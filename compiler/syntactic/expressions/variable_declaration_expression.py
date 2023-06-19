from .expression import Expression
from .type_specifier_expression import TypeSpecifierExpression

class VariableDeclarationExpression(Expression):
   def __init__(self, tokens) -> None:
      self.tokens = tokens

   def interpret(self):
      print("In Variable Declaration Expression")
      type_specifier_expression = TypeSpecifierExpression(self.tokens)
      # variable_declaration_expression = VariableDeclarationExpression(self.tokens)
      if type_specifier_expression.interpret(): 
         print(f"TOKEN: {self.tokens[0].name}")
         return True
      return False