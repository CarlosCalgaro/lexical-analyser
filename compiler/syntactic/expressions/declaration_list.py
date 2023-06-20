from .expression import Expression
from compiler import TokenList as Tk
from .declaration import Declaration
class DeclarationList(Expression):

   def interpret(self):
      if self.interpret_expression(Declaration):
         self.interpret_expression(DeclarationList)
         return True
      return False
   
   def level(self):
      return 2