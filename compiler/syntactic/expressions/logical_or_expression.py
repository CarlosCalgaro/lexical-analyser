from .expression import Expression
from .language_expression_d import LanguageExpressionD
from .assignment_expression import AssignmentExpression
from compiler import TokenList as Tk

class LogicalOrExpression(Expression):

   def interpret(self):
      if self.interpret_expression(AssignmentExpression):
         if self.interpret_expression(LanguageExpressionD):
            return True
      return False