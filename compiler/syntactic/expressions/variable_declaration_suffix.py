from .expression import Expression
from compiler import TokenList as Tk

class VariableDeclarationSuffix(Expression):

   def interpret(self):
      if (self.check_tokens(Tk.TK_OPEN_BRACKET) and
         self.check_tokens([Tk.TK_ID, Tk.TK_CONST]) and
         self.check_tokens(Tk.TK_CLOSE_BRACKET)):
         return True
      return False