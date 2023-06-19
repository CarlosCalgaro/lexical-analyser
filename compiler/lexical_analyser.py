from compiler import Token, TOKENS, TokenList as Tk
from compiler.errors import LexicalErrorException
import re
import sys
class LexicalAnalyser:
   token_list = []
   file = None
   output_stream = sys.stdout

   def __init__(self, output_stream=None) -> None:
      self.output_stream = output_stream
   
   def compile(self, input_stream):
      line= 1 ; column = 1
      self.file = input_stream.read()
      while(self.file != ""):
         token = self.extract_token()
         if(token[0] not in [Tk.TK_NEWLINE, Tk.TK_WHITESPACE]):
            self.token_list.append(Token(token[0], token[1], line, column))
         if token[0] == Tk.TK_NEWLINE:
            line +=1
            column = 1
         else:
            column += token[1].end()
      self.token_list.append(Token(Tk.TK_EOF, None, line, column))
      return self.token_list

   def extract_token(self):
      for tkn_value, regex in TOKENS:
         match = re.search(regex, self.file)
         if match:
            self.file = re.sub(regex, '', self.file)
            return (tkn_value, match)
      raise LexicalErrorException(self.file)

   def print(self):
      template = "{0:10} {1:10} {2:28} {3:10}"
      self.output_stream.write(f"{template.format('LINHA', 'COLUNA', 'LEXEMA', 'TOKEN')}\n")
      for token in self.token_list:
         self.output_stream.write(f"{template.format(token.line, token.column, token.name, token.string() )}\n")