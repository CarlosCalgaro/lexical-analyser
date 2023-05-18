from compiler import TOKENS as c_tokens
import re

class Compiler:
   token_list = []
   current_line = 0
   current_line_pos = 0

   def compile(self, file):
      lines = file.readlines()
      for line in lines:
         self.current_line_pos = 0
         self.current_line += 1
         while line != "":
            try:
               line = self.extract_token(line)
            except SyntaxError as e:
               self.print_list()
               raise e
      self.print_list()

   def extract_token(self, string):
      for tkn_value, regex in c_tokens:
            match = re.search(regex, string)
            if match:
               span = match.span(0)
               self.token_list.append((self.current_line, self.current_line_pos, tkn_value, match ))
               self.current_line_pos = self.current_line_pos + span[1]
               return re.sub(regex, '', string).strip()
      raise SyntaxError(f"can't find any token in: {string}")

   def print_list(self):
      print(f"Linha\tColuna\tLexema\t\tToken")
      for match in self.token_list:
         print(f"{match[0]}\t {match[1]} \t {match[3].group(0)} \t {match[2]}")






