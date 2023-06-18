from abc import abstractmethod

class SyntacticAnalyser:

   def __init__(self, token_list) -> None:
      self.token_list = token_list

   @abstractmethod
   def analyse(self) -> bool:
      raise NotImplementedError
   
   def token(self):
      return self.token_list[0][1]

   def consume_token(self):
      return self.token_list.pop(0)