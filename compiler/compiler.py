from compiler import TOKENS as c_tokens
import re
import sys

class Compiler:
   token_list = []
   current_line = 0
   current_line_pos = 0
   lines = None
   output_stream = sys.stdout

   def __init__(self, output_stream=None) -> None:
      self.output_stream = output_stream
   
   def compile(self, input_stream):
      self.lines = input_stream.read()
      while(self.lines != ""):
         token = self.extract_token()
         self.token_list.append(token)
      self.print()

   def extract_token(self):
      self.lines = self.lines.strip()
      for tkn_value, regex in c_tokens:
         re_match = re.search(regex, self.lines)
         if re_match:
            self.lines = re.sub(regex, '', self.lines)
            return (re_match, tkn_value)
      raise SyntaxError(f"can't find a match for: {self.lines}")

   def print(self):
      self.output_stream.write(f"Linha\tColuna\tLexema\t\tToken\n")
      for match in self.token_list:
         self.output_stream.write(f"{match[1]}: {str(match[0])}\n")






