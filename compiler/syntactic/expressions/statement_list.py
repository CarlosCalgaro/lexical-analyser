from .expression import Expression
from compiler import TokenList as Tk
from .statement import Statement
class StatementList(Expression):

   def interpret(self):
      if self.interpret_expression(Statement):
         if self.interpret_expression(StatementList):
            return True
         return True
      return False