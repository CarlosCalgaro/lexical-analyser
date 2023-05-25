import sys
from compiler import Compiler
import argparse

if __name__ == '__main__':
   parser = argparse.ArgumentParser(description='Lexical Compiler C')
   parser.add_argument('source_file', help='Path to the source file (e.g., ./main.c)')
   parser.add_argument('--output', help='Path to the output file (e.g., output.txt)')
   args = parser.parse_args()

   input_stream = open(args.source_file, 'r')
   if(args.output):
      output_stream = open(args.output, 'w')
   else:
      output_stream = sys.stdout
   compiler = Compiler(output_stream=output_stream)
   compiler.compile(input_stream)

   input_stream.close()
   output_stream.close()