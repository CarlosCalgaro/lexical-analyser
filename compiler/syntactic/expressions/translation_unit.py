from .expression import Expression
from .declaration_list import DeclarationList
from compiler import TokenList as Tk

class TranslationUnit(Expression):

   def interpret(self):
      if self.interpret_expression(DeclarationList) and self.check_tokens(Tk.TK_EOF):
         return True
      return False
   
   def level(self):
      return 1