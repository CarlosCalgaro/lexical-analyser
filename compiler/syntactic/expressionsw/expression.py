from abc import abstractmethod

class Expression():
   def __init__(self, tokens):
      self.tokens = tokens

   @abstractmethod
   def interpret(self):
      raise NotImplementedError

   def current_token(self):
      return self.tokens[0]

   def current_token_name(self):
      if self.current_token is None:
         return None
      else:
         return self.tokens[0].name

   def interpret_expression(self, expression_type, replace_tokens = True):
      expression = expression_type(self.tokens)
      print(f"Evaluating: {expression_type.__name__}")
      evalued = expression.interpret()
      if replace_tokens:
         self.tokens = expression.tokens
      return evalued
   
   # def interpret_tokens(self, token_list):

   def consume_token(self):
      self.tokens = self.tokens[1:]

   def print_tree(self, name, custom_tab=0):
      tabs = '\t' * custom_tab
      print(f"{tabs}{name}")

   def print_expected_token(self, expected_token = None):
      print(f"ERROR: Unexpected token {self.current_token_name()}, Expected: {expected_token}")