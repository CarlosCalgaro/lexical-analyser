from .expression import Expression
from .logical_or_expression import LogicalOrExpression
from compiler import TokenList as Tk

class ConditionalExpression(Expression):

   def interpret(self):
      if self.interpret_expression(LogicalOrExpression):
         return True
      return False