import ast

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
    __traverse_graph_utility(package,filename,counter)
    return counter.function_params


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

    def generic_visit(self,node):
        self.information_count += 1
        super().generic_visit(node)



def get_global_code_volume(package:str,filename:str) -> int:
    visitor = GlobalCodeVisitor()
    __traverse_graph_utility(package,filename,visitor)
    return visitor.information_count


def __traverse_graph_utility(package:str,filename:str, visitorType:ast.NodeVisitor) -> None:
    """
    Utility function to handle generic ast parsing
    """
    with open(f"{package}/{filename}") as file:
        source = file.read()
        tree = ast.parse(source)
        visitor = visitorType
        visitor.visit(tree)

    
