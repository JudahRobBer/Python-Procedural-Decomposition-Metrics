import ast

class accessofForeignData(ast.NodeVisitor):
  def __init__(self):
    self.func_name = ""
    self.assigned = []
    self.foreign_access_count = {}

  # Adds a new key to the return dictionary for each function.
  # Resets the list of variables defined in that function.
  def visit_FunctionDef(self, node):
    self.func_name = node.name
    self.assigned = []
    self.foreign_access_count[self.func_name] = 0 

  # Increments the AOFD by one for each call of an outside function.
  def visit_Call(self,node):
    if (node.func.id != "print"):
      self.foreign_access_count[self.func_name] += 1
    self.generic_visit(node)

  # Adds assigned variables to the corresponding list. When these variables appear later in the function, they do not increase the AOFD.
  def visit_Assign(self, node):
    if (not self.assigned.__contains__(node.targets[0].id)):
      self.assigned.append(node.targets[0].id)
    self.generic_visit(node)

  # Increments the AOFD for the corresponding function when a variable not defined in it is accessed.
  def visit_Name(self, node):
    if ((not self.assigned.__contains__(node.id)) and node.id != "print"):
      self.foreign_access_count[self.func_name] += 1
    self.generic_visit(node)

  def get_Foreign_Access(self, package: str, filename: str):
    with open(f"{package}/{filename}") as file:
      source_code = file.read()
       
      tree = ast.parse(source_code)
      checker = accessofForeignData()

      checker.generic_visit(tree)
      # Returns a dictionary of each function and the corresponding number of references to values defined outside of that function.
      return (checker.foreign_access_count)
