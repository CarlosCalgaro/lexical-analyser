
from .expression import Expression
from compiler import TokenList as Tk

class LogicalAndExpression(Expression):

   def interpret(self):
      return True