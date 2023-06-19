from .expression import Expression
from compiler import TYPE_SPECIFIER_LIST
from .type_specifier_long_expression import TypeSpecifierLongExpression

class TypeSpecifierExpression(Expression):

   def interpret(self):
      self.print_tree('Type Specifier', 4)
      if self.interpret_type_specifier_long():
         return True
      elif self.current_token_name() in TYPE_SPECIFIER_LIST:
        self.print_tree(f" - Consumed {self.current_token_name()}", 5)
        self.consume_token()
        return True
      return False
   
   def interpret_type_specifier_long(self):
      type_specifier_long_expression = TypeSpecifierLongExpression(self.tokens)
      if type_specifier_long_expression.interpret():
         self.tokens = type_specifier_long_expression.tokens
         return True
      return False