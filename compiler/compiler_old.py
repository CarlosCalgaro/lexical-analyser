from compiler import TOKENS as c_tokens
import re

class Compiler:
   token_list = []

   def compile(self, file):
      lines = file.readLines()
      line_count = 0
      for line in lines:
         line_count += 1
         while code != "":
            try:
               code = self.extract_token(code)
            except SyntaxError as e:
               self.print_list()
               raise e
      self.print_list()

   def extract_token(self, string):
      for tkn_value, regex in c_tokens:
            match = re.search(regex, string)
            if match:
               self.token_list.append((tkn_value, regex, match))
               return re.sub(regex, '', string).strip()
      raise SyntaxError(f"can't find any token in: {string}")
   
   def print_list(self):
      for match in self.token_list:
         print(f"token: {match[0]} with: {match[1]} match:{match[2]}")
















   # def match_token(self, str):
   #    while(str != ""):
   #       for tkn_value, regex in c_tokens:
   #          match = re.search(regex, str)
   #          print(f"Matching {regex} on {str}")
   #          if match:
   #             self.token_list.append((tkn_value, regex, match))
   #             str = re.sub(regex, '', str).strip()
   #             continue
   #       raise SyntaxError(f"can't find any token in: {str}")
   #          # self.token_list.append((tkn_value, regex, token))
   #          # return
         