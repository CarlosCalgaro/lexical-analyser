from .expression import Expression
from .variable_declaration import VariableDeclaration
from .function_declaration import FunctionDeclaration
class Declaration(Expression):

   def interpret(self):
      if (self.interpret_expression(VariableDeclaration)):
         return True
      if (self.interpret_expression(FunctionDeclaration)):
         return True
      return False

   def level(self):
      return 3