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

  def consume_token(self):
    self.tokens = self.tokens[1:]

  def print_tree(self, name, custom_tab=0):
    tabs = '\t' * custom_tab
    print(f"{tabs}{name}")