from .expression import Expression
from .declaration_expression import DeclarationExpression

class DeclarationListExpression(Expression):

   def interpret(self):
      self.print_tree('Declaration List Expression', 1)
      declaration_expression = DeclarationExpression(self.tokens)
      if declaration_expression.interpret():
         self.tokens = declaration_expression.tokens
         declaration_list_expression = DeclarationListExpression(self.tokens)
         if declaration_list_expression.interpret():
            self.tokens = declaration_list_expression.tokens
         return True
      return False