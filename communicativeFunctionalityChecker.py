import ast

class CommunicativeFunctionalityChecker(ast.NodeVisitor):
  def __init__(self):
    self.vars_accessed = []

  def visit_Name(self, node):
    self.vars_accessed.append(node.id)
    
    self.generic_visit(node)

  def getCommunicativeFunctionality(self, package:str, filename: str):
    with open(f"{package}/{filename}") as file:
      source_code = file.read()
       
      tree = ast.parse(source_code)
      checker = CommunicativeFunctionalityChecker()
      checker.visit(tree)

      return len(checker.vars_accessed)
    
