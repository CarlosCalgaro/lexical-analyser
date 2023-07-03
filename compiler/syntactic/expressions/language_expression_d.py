from .expression import Expression
from .assignment_expression import AssignmentExpression
from compiler import TokenList as Tk

class LanguageExpressionD(Expression):

   def interpret(self):
      if self.check_tokens(Tk.TK_COMMA):
         if self.interpret_expression(AssignmentExpression):
            if self.interpret_expression(LanguageExpressionD):
               return True
            return False
         return False
      return True
