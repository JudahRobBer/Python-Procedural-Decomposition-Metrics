import ast

class FunctionParameterCounter(ast.NodeVisitor):
    def __init__(self):
        self.function_params = {}

    def visit_FunctionDef(self, node):
        # Count the number of parameters
        param_count = len(node.args.args)
        # Get the function name
        function_name = node.name
        # Store the result
        self.function_params[function_name] = param_count
        # Continue to visit child nodes
        self.generic_visit(node)

def get_function_parameter_counts(package:str,filename:str):
    with open(f"{package}/{filename}") as file:
        source_code = file.read()
       
        tree = ast.parse(source_code)
        counter = FunctionParameterCounter()
        counter.visit(tree)
        
        return counter.function_params
