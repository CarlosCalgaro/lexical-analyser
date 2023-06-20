from abc import abstractmethod
from compiler import Token

class Expression():
   def __init__(self, tokens) -> None:
      self.tokens = tokens

   @abstractmethod
   def current_token(self) -> Token:
      return self.tokens[0]

   def consume_token(self) -> None:
      self.tokens = self.tokens[1:]

   def current_token_name(self) -> str:
      return self.current_token().name if self.current_token() else None

   def interpret_expression(self, expression_type, replace_tokens = True) -> bool:
      expression = expression_type(self.tokens)
      print(f"Evaluating: {expression_type.__name__}")
      evaluated = expression.interpret()
      if replace_tokens:
         self.tokens = expression.tokens
      return evaluated

   def check_tokens(self, tokens = []) -> bool:
      if type(tokens) is Token: tokens = [tokens]
      if type(tokens) is list:
         return self.current_token_name() in tokens
      else:
         raise AttributeError('token must be a token or list of tokens')
