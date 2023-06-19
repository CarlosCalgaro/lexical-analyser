from .expression import Expression
from compiler import ASSIGNABLES_LIST


class VariableNameExpression(Expression):

  def interpret(self):
    self.print_tree("Variable Name", 4)
    if self.current_token_name() in ASSIGNABLES_LIST:
      self.print_tree(f" - Consumed: {self.current_token_name()}", 5)
      self.consume_token()
      return True
    return False
