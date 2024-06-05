import ast

class CommunicativeFunctionalityChecker(ast.NodeVisitor):
  def __init__(self):
    self.vals_accessed = []
    self.unique_vals = []

  def checkUniques(self, name:str):
    if (not self.unique_vals.__contains__(name)) :
      self.unique_vals.append(name)
  
  def visit_Name(self, node):
    self.vals_accessed.append(node.id)
    
    checkUniques(node.id)
    self.generic_visit(node)
  
  def getCommunicativeFunctionality(self, package:str, filename: str):
    with open(f"{package}/{filename}") as file:
      source_code = file.read()
       
      tree = ast.parse(source_code)
      checker = CommunicativeFunctionalityChecker()
      checker.visit(tree)

      return float(len(checker.unique_vals) / len(checker.vals_accessed))
    
