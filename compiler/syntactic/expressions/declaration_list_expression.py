from .expression import Expression
from .declaration_expression import DeclarationExpression

class DeclarationListExpression(Expression):

   def interpret(self):
      declaration_expression = DeclarationExpression(self.tokens)
      print("In Declaration List Expression")
      if declaration_expression.interpret():
         self.tokens = declaration_expression.tokens
         declaration_list_expression = DeclarationListExpression(self.tokens)
         if declaration_list_expression.interpret():
            self.tokens = declaration_list_expression.tokens
            return True
         return True
      return False
      # result, tokens = declaration_expression.interpret()
      # self.tokens = tokens
      # if result:
      #    declaration_list_expression = DeclarationListExpression(self.tokens)
      #    result, tokens = declaration_list_expression.interpret()
      #    self.tokens = tokens
      #    if result:
      #       return True, self.tokens
      #    return True, self.tokens
      # return False, self.tokens
