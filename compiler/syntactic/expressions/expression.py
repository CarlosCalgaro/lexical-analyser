from abc import abstractmethod
from compiler import Token, TokenList
class Expression():
   def __init__(self, tokens) -> None:
      self.tokens = tokens
      self.consumed_tokens = []

   @abstractmethod
   def current_token(self) -> Token:
      return self.tokens[0]

   def consume_token(self) -> None:
      self.tokens = self.tokens[1:]

   def current_token_name(self) -> str:
      return self.current_token().name if self.current_token() else None

   def interpret_expression(self, expression_type, replace_tokens = True) -> bool:
      expression = expression_type(self.tokens)
      self.print_evaluate(expression_type)
      evaluated = expression.interpret()
      if evaluated and replace_tokens:
         self.tokens = expression.tokens
         self.consumed_tokens = self.consumed_tokens + expression.consumed_tokens
      return evaluated

   def check_tokens(self, tokens = []) -> bool:
      if isinstance(tokens, TokenList): tokens = [tokens]
      if type(tokens) is list:
         if self.current_token_name() in tokens:
            # print(f"Consuming token: {self.current_token_name()}")
            self.consumed_tokens.append(self.current_token())
            self.consume_token()
            return True
         # print(f"Token not found, expected: {tokens}, found {self.current_token_name()}")
         return False
      else:
         raise AttributeError('token must be a token or list of tokens')
   def level(self):
      return 0
   
   def print_token_list(self):
      # print(' '.join([x.name for x in self.consumed_tokens]))
      print(' '.join([x.string() for x in self.consumed_tokens]))

   def print_evaluate(self, expression_type):
      tabs = '\t' * self.level()
      # print(f"{tabs} Evaluating: {expression_type.__name__}")