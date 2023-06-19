from .expression import Expression
from .variable_declaration_expression import VariableDeclarationExpression
# from compiler.syntactic.expressions import Expression

from compiler import TokenList as Tk

class DeclarationExpression(Expression):

   def interpret(self):
      self.print_tree('Declaration Expression', 2)

      variable_declaration_expression = VariableDeclarationExpression(self.tokens)
      if variable_declaration_expression.interpret():
         self.tokens = variable_declaration_expression.tokens
         return True
      elif False: # Function Declaration
        return False
      return False