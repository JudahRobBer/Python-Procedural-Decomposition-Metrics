import ast
import statistics

class accessofForeignData(ast.NodeVisitor):
  def __init__(self):
    self.assigned = []
    self.function_names = ["global"]
    self.foreign_access_count = [0]
    self.allowed_names = ["print","range","import","len","int","str","float","self"]

  # Adds a new key to the return dictionary for each function.
  # Resets the list of variables defined in that function.
  def visit_FunctionDef(self, node):
    self.assigned = []
    self.foreign_access_count.append(0) 
    self.function_names.append(node.name)
    self.generic_visit(node)

  # Program should not count repeated calls of an imported library's methods as foreign.
  def visit_Import(self, node):
    self.generic_visit(node)
    self.allowed_names.append(node.names[0].name)

  # Adds index variables corresponding to for loops to the "assigned" list.
  def visit_For(self, node):
    if (not self.assigned.__contains__(node.target.id)):
      self.assigned.append(node.target.id)
    self.generic_visit(node)

  # Adds assigned variables to the corresponding list. When these variables appear later in the function, they do not increase the AOFD.
  def visit_Assign(self, node):
    if isinstance(node.targets[0], ast.Tuple):
      for element in node.targets[0].elts :
        if (not self.assigned.__contains__(element)):
          self.assigned.append(element)
    elif (not self.assigned.__contains__(node.targets[0].id)):
      self.assigned.append(node.targets[0].id)
    self.generic_visit(node)

  # Increments the AOFD for the corresponding function when a variable not defined in it is accessed.
  def visit_Name(self, node):
    if (not self.assigned.__contains__(node.id)) and (not self.allowed_names.__contains__(node.id)):
      self.foreign_access_count[len(self.foreign_access_count) - 1] += 1
    self.generic_visit(node)

  def get_Foreign_Access(self, package: str, filename: str):
    with open(f"{package}/{filename}") as file:
      source_code = file.read()
       
      tree = ast.parse(source_code)

      self.generic_visit(tree)
      
  #Returns the average count of foreign elements accessed across file methods.
  def ret_Mean_Access(self):
    return statistics.mean(self.foreign_access_count)

  #Returns the standard deviation of foreign elements that are accessed across file methods.
  def ret_St_Dev_Access(self):
    if len(self.foreign_access_count) > 1:
      return statistics.stdev(self.foreign_access_count)
    return -1.0

  #Returns the maximum of foreign elements accessed across file methods.
  def ret_Max_Access(self):
    return max(self.foreign_access_count)

  #Returns the name of the method with the maximum foreign elements accessed.
  def ret_Max_Name(self):
    maximum = self.ret_Max_Access()

    for quant in range(len(self.foreign_access_count)):
      if self.foreign_access_count[quant] == maximum :
        return self.function_names[quant]
