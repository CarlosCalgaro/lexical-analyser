from .expression import Expression
from compiler import TokenList as Tk

class LanguageExpression(Expression):
   def interpret(self):
      return True