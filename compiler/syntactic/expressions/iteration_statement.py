from .expression import Expression
from compiler import TokenList as Tk
from .language_expression import LanguageExpression
# from .statement import Statement as Stat

class IterationStatement(Expression):
   def interpret(self):
      if self.while_expression():
         return True
      return False

   def while_expression(self):
      if self.check_tokens(Tk.TK_WHILE) and self.check_tokens(Tk.TK_OPEN_PARENTHESIS):
         if self.interpret_expression(LanguageExpression):
            if self.check_tokens(Tk.TK_CLOSE_PARENTHESIS):
               # if self.interpret_expression(Stat):
               #    return True
                  return True
      return False
