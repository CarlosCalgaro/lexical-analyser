from .expression import Expression
from compiler import TokenList as Tk

class CompoundStatement(Expression):

   def interpret(self):
      return True