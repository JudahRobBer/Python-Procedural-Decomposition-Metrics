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


def get_function_parameter_counts(package:str,filename:str):
    with open(f"{package}/{filename}") as file:
        source_code = file.read()
       
        tree = ast.parse(source_code)
        counter = FunctionParameterCounter()
        counter.visit(tree)
        
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

    def get_total_global_code(self):
        return self.information_count


def get_global_code_volume(package:str,filename:str) -> int:
    with open(f"{package}/{filename}") as file:
        source = file.read()
        tree = ast.parse(source)
        
        visitor = GlobalCodeVisitor()
        visitor.visit(tree)
        
        return visitor.get_total_global_code()



