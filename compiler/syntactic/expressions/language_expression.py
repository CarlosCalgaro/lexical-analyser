from .expression import Expression
from .conditional_expression import ConditionalExpression
from compiler import TokenList as Tk

class LanguageExpression(Expression):

   def interpret(self):
      if self.interpret_expression(ConditionalExpression):
            return True
      return False