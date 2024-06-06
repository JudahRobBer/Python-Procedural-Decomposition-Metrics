import ast

class accessofForeignData(ast.NodeVisitor):
  def __init__(self):
    self.assigned = []
    self.foreign_access_count = 0
    
  def visit_Assign(self, node):
    if (not self.assigned.__contains__(node.targets[0].id)):
      self.assigned.append(node.targets[0].id)
    self.generic_visit(node)

  def visit_Name(self, node):
    if ((not self.assigned.__contains__(node.id)) && node.id != "print"):
      self.foreign_access_count += 1
    self.generic_visit(node)

  def get_Foreign_Access(self, package: str, filename: str):
    with open(f"{package}/{filename}") as file:
      source_code = file.read()
       
      tree = ast.parse(source_code)
      checker = accessofForeignData()

      checker.visit(tree)

      return (checker.foreign_access_count)
