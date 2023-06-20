from .expression import Expression
from .type_specifier_expression import TypeSpecifierExpression
from .variable_name_expression import VariableNameExpression
from compiler import TokenList as Tk
from .variable_declaration_prefix_expression import VariableDeclarationPrefixExpression
from .variable_declaration_suffix_expression import VariableDeclarationSuffixExpression

class VariableDeclarationExpression(Expression):

   def interpret(self):
      self.print_tree('Variable Declaration', 3)
      if self.interpret_type_specifier():
        if self.interpret_variable_declaration_prefix() and self.interpret_variable_name() and self.interpret_variable_declaration_suffix():
          if self.current_token_name() == Tk.TK_SEMICOLON:
             self.print_tree(f" - Consumed {self.current_token_name()}", 4)
             self.consume_token()
             return True
          else:
            self.print_expected_token()
            #  print(f"Unexpected token: {self.current_token_name()}")
      return False
   def interpret_variable_declaration_suffix(self):
      variable_declaration_suffix = VariableDeclarationSuffixExpression(self.tokens)
      if variable_declaration_suffix.interpret():
         self.tokens = variable_declaration_suffix.tokens
         return True
      return False

   def interpret_variable_declaration_prefix(self):
      variable_declaration_prefix = VariableDeclarationPrefixExpression(self.tokens)
      if variable_declaration_prefix.interpret():
         self.tokens = variable_declaration_prefix.tokens
         return True
      return False

   def interpret_variable_name(self):
      variable_name_expression = VariableNameExpression(self.tokens)
      if variable_name_expression.interpret():
         self.tokens = variable_name_expression.tokens
         return True
      else:
         return False

   def interpret_type_specifier(self):
      type_specifier_expression = TypeSpecifierExpression(self.tokens)
      if type_specifier_expression.interpret():
         self.tokens = type_specifier_expression.tokens
         return True
      else:
         return False