import ast

def check_Uniques(lis:list, name:str):
      if (not lis.__contains__(name)) :
        lis.append(name)

# Represents the number of times each unique variable referenced in the method is referenced. 
# Low values represents low amounts of cohesion and a possible problem with the method.
class CommunicativeFunctionalityChecker(ast.NodeVisitor):

      
  def __init__(self):
    self.vals_accessed = {}
    self.unique_vals = {}
    self.communicative_functionality = {}
    self.func_name = "global"

  def visit_FunctionDef(self, node):
    self.func_name = node.name
    self.vals_accessed[self.func_name] = []
    self.unique_vals[self.func_name] =[]
      
  def visit_Name(self, node):
  
    self.vals_accessed[self.func_name].append(node.id)
    
    check_Uniques(self.unique_vals[self.func_name],node.id)
    self.generic_visit(node)
        
  def getCommunicativeFunctionality(self, package:str, filename: str):
    with open(f"{package}/{filename}") as file:
      source_code = file.read()
       
      tree = ast.parse(source_code)
      checker = CommunicativeFunctionalityChecker()
      checker.visit(tree)

      for func in self.vals_accessed :
            self.communicative_functionality[func] = len(self.vals_accessed[func]) / len(self.unique_vals[func])

      return self.communicative_functionality
    
