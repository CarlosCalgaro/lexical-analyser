from .expression import Expression
from .statement import Statement
from compiler import TokenList as Tk

class StatementList(Expression):

   def interpret(self):
      if self.interpret_expression(Statement):
         if self.interpret_expression(StatementList):
            return True
         return True
      return False