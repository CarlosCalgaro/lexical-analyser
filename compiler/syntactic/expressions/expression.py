from abc import abstractmethod

class Expression():

   def __init__(self, tokens):
      self.tokens = tokens

   @abstractmethod
   def interpret(self):
      raise NotImplementedError
   
   def current_token_name(self):
      self.tokens[0].name

   def consume_token(self):
      self.tokens = self.tokens[1:]
