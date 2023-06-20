from .expression import Expression
from .declaration_list import DeclarationList
from compiler import TokenList as Tk

class TranslationUnit(Expression):

   def interpret(self):
      if self.interpret_expression(DeclarationListExpression):
         if self.check_tokens(Tk.TK_EOF):
            return True
      return False