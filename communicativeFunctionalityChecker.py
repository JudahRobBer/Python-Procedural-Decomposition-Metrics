import ast

def check_Uniques(lis:list, name:str):
      if (not lis.__contains__(name)) :
        lis.append(name)

class CommunicativeFunctionalityChecker(ast.NodeVisitor):
  def __init__(self):
    self.vals_accessed = []
    self.unique_vals = []
  
  def visit_Name(self, node):
  
    self.vals_accessed.append(node.id)
    
    check_Uniques(self.unique_vals,node.id)
    self.generic_visit(node)
        
  def getCommunicativeFunctionality(self, package:str, filename: str):
    with open(f"{package}/{filename}") as file:
      source_code = file.read()
       
      tree = ast.parse(source_code)
      checker = CommunicativeFunctionalityChecker()
      checker.visit(tree)

      return float(len(checker.unique_vals) / len(checker.vals_accessed))
    
