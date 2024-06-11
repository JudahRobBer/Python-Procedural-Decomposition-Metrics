import ast

# Generic Utilities ------------------------------------------------------
def traverse_graph_utility(package:str,filename:str, visitorType:ast.NodeVisitor) -> None:
    """
    Utility function to handle generic ast parsing
    """
    with open(f"{package}/{filename}") as file:
        source = file.read()
        tree = ast.parse(source)
        visitor = visitorType
        visitor.visit(tree)



# Function Parameter Counting ----------------------------------------

class FunctionParameterCounter(ast.NodeVisitor):
    def __init__(self):
        self.function_params = {}

    def visit_FunctionDef(self, node):
        # Count the number of parameters
        param_count = len(node.args.args)
        function_name = node.name
        self.function_params[function_name] = param_count
    
        self.generic_visit(node)


def get_function_parameter_counts(package:str,filename:str) -> dict:
    """
    generates a map of function names to their parameter counts
    """
    counter = FunctionParameterCounter()
    traverse_graph_utility(package,filename,counter)
    return counter.function_params


# Global Code Volume Counting -------------------------------------

class GlobalCodeVisitor(ast.NodeVisitor):
    
    def __init__(self):
        """
        rather than counting lines, count the number of global nodes of the AST
        """
        self.information_count = 0
    
    def visit_FunctionDef(self,node):
        """
        ignore function definitions and all the code contained within them
        """
        pass

    def visit_Import(self,node):
        pass
        

    def generic_visit(self,node):
        self.information_count += 1
        super().generic_visit(node)



def get_global_code_volume(package:str,filename:str) -> int:
    visitor = GlobalCodeVisitor()
    traverse_graph_utility(package,filename,visitor)
    return visitor.information_count

class ReturningFunctionsVisitor(ast.NodeVisitor):
    """
    Get the set of all functions with return values
    """

    def __init__(self):
        self.returning_functions = set()
        self.current_function = None

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.current_function = node.name
        self.generic_visit(node)
    
    def visit_Return(self,node:ast.Return):
        self.returning_functions.add(self.current_function)
        self.generic_visit(node)


class PrintingFunctionsVisitor(ast.NodeVisitor):
    """
    Gets the set of all functions with print statements
    """
    def __init__(self):
        self.printing_functions = set()
        self.current_function = None


    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.current_function = node.name
        self.generic_visit(node)
    
    def visit_Call(self,node:ast.FunctionDef):
        if node.func.id == "print":
            self.printing_functions.add(self.current_function)
        self.generic_visit(node)

    
    

def get_multiple_output_functions(package:str,filename:str) -> set:
    returning_visitor = ReturningFunctionsVisitor()
    traverse_graph_utility(package,filename,returning_visitor)
    returning_functions = returning_visitor.returning_functions
    
    printing_visitor = PrintingFunctionsVisitor()
    traverse_graph_utility(package,filename,printing_visitor)
    printing_functions = printing_visitor.printing_functions

    violating_functions = returning_functions.intersection(printing_functions)

    return violating_functions

    
    

        





    
