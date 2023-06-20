from .expression import Expression
from .type_specifier import TypeSpecifier
from compiler import TokenList as Tk
class VariableDeclarationPrefix(Expression):

   def interpret(self):
      if self.check_tokens(Tk.TK_ASTERISK):
         self.interpret_expression(VariableDeclarationPrefix)
      return True