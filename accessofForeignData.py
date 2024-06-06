import ast

class accessofForeignData(ast.NodeVisitor):
  def__init__(self):
    self.assigned = []
    self.foreign_access_count = 0
    
  def visit_Assign(self, node):
    if (not self.assigned.__contains__(node.targets[0].id)):
      self.assigned.append(node.targets[0].id)
