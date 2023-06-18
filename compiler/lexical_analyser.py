from compiler import Token, TOKENS, TokenList as Tk
from compiler.errors import LexicErrorException
import re
import sys
class LexicalAnalyser:
   token_list = []
   file = None
   output_stream = sys.stdout

   def __init__(self, output_stream=None) -> None:
      self.output_stream = output_stream
   
   def compile(self, input_stream):
      try:
         self.file = input_stream.read()
         while(self.file != ""):
            token = self.extract_token()
            self.token_list.append(token)
         return self.token_list
      except LexicErrorException as e:
         self.print()
         return []

   def extract_token(self):
      for tkn_value, regex in TOKENS:
         match = re.search(regex, self.file)
         if match:
            self.file = re.sub(regex, '', self.file)
            return Token(tkn_value, match) 
      raise LexicErrorException(self.file)

   def print(self):
      template = "{0:10} {1:10} {2:28} {3:10}"
      self.output_stream.write(f"{template.format('LINHA', 'COLUNA', 'LEXEMA', 'TOKEN')}\n")
      for token in self.token_list:
         self.output_stream.write(f"{template.format(token.line, token.column, token.name, token.string() )}\n")

      # line = 1
      # column = 1
      # for found_token in self.token_list:
      #    match = found_token[0]
      #    token = found_token[1]
      #    string = match.group(0)
      #    if(token not in [Tk.TK_NEWLINE, Tk.TK_WHITESPACE]):
      #       self.output_stream.write(f"{template.format(line, column, token, string)}\n")
      #    if(token == Tk.TK_WHITESPACE):
      #       line += 1
      #       column = 1
      #    else:
      #       column += match.end()