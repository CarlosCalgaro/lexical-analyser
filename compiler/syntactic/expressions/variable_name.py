from .expression import Expression
from compiler import ASSIGNABLES_LIST


class VariableName(Expression):

   def interpret(self):
      if self.check_tokens(ASSIGNABLES_LIST):
         return True
      return False