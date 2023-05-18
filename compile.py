import sys
from compiler import Compiler

if __name__ == '__main__':
   path = sys.argv[1]
   compiler = Compiler()
   with open(path, 'r') as file:
      compiler.compile(file)
