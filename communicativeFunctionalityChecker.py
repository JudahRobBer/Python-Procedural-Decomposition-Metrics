import ast
from ast_analysis import traverse_graph_utility


def check_Uniques(lis:list, name:str):
      if (not lis.__contains__(name)) :
        lis.append(name)

# Represents the number of times each unique variable referenced in the method is referenced. 
# Low values represents low amounts of cohesion and a possible problem with the method.
class CommunicativeFunctionalityChecker(ast.NodeVisitor):

  #Initializes the dictionaries and a value for the function name. Code that appears before the first function defiinition is global.    
  def __init__(self):
    self.vals_accessed = {"global":[]}
    self.unique_vals = {"global":[]}
    self.communicative_functionality = {}
    self.func_name = "global"

  #Sets the function name to the current function upon entrance. Creates arrays in the dictionaries to keep track of variable usage.
  def visit_FunctionDef(self, node):
    self.func_name = node.name
    self.vals_accessed[self.func_name] = []
    self.unique_vals[self.func_name] = []

    self.generic_visit(node)

  #Should not process built in functions as variables, but should process attribute calls on collections.
  def visit_Call(self, node):
    if self.unique_vals.__contains__(((ast.Name)(node.func)).id):
      self.generic_visit(node)
    else:
      if len(node.args) > 0:
        self.generic_visit(node.args[0])

  #Should not process imports.
  def visit_Import(self,node):
    pass

  #Registers every variable, adding them to the vals_accessed list for the function and the corresponding unique_vals list if appropriate.
  def visit_Name(self, node):
  
    self.vals_accessed[self.func_name].append(node.id)
    
    check_Uniques(self.unique_vals[self.func_name],node.id)
    self.generic_visit(node)

  #Calculates the communicative functionality for each method and returns the results in a list.
def getCommunicativeFunctionality(package:str, filename: str):
  checker = CommunicativeFunctionalityChecker()
  traverse_graph_utility(package,filename,checker)
  

  for func in checker.vals_accessed :
    checker.communicative_functionality[func] = len(checker.vals_accessed[func]) / len(checker.unique_vals[func])

  return checker.communicative_functionality
