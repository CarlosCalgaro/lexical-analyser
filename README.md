# Lexical Compiler

This is a lexical compiler implemented in Python. It reads a source file, extracts tokens, and outputs the results.

## Prerequisites

- Python 3.x

## Usage
```
python compile.py source_file [--output output_file]
```
- `source_file`: Path to the source file (e.g., ./main.c).
- `--output output_file`: (Optional) Path to the output file (e.g., output.txt). If not specified, the output will be printed to the console.

## How it works

1. The program uses regular expressions to extract tokens from the source file.
2. It reads the source file line by line and extracts tokens using predefined regular expressions.
3. The extracted tokens are stored in a list for further processing.
4. Finally, it prints the extracted tokens along with their corresponding line number, column number, lexeme, and token type.

## Example

To compile a source file and generate the output, run the following command:

```
python compile.py ./main.c --output output.txt
```

This will read the `main.c` file, extract tokens, and write the output to the `output.txt` file.

If you don't specify the `--output` argument, the output will be printed to the console.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.