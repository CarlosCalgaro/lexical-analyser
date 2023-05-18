import re

# Definindo os tokens como expressões regulares
tokens = [
    ('tkint', r'int'),
    ('tkfloat', r'float'),
    ('tkchar', r'char'),
    ('tkdouble', r'double'),
    ('tkstruct', r'struct'),
    ('tkid', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('tkop', r'[+\-*/%]'),
    ('tkassign', r'='),
    ('tksemicolon', r';'),
    ('tkcomma', r','),
    ('tkopenparen', r'\('),
    ('tkcloseparen', r'\)'),
    ('tkopenbrace', r'{'),
    ('tkclosebrace', r'}'),
    ('tkintconst', r'\d+'),
    ('tkarrow', r'->'),
    ('tkgreater', r'>'),
    ('tkless', r'<'),
    ('tkequal', r'=='),
    ('tknotequal', r'!='),
    ('tkand', r'&&'),
    ('tkor', r'\|\|'),
    ('tknot', r'!'),
    ('tkcase', r'case'),
    ('tkdefault', r'default')
]

def tokenize(code):
    tokens_found = []

    # Removendo espaços em branco e comentários
    code = re.sub(r'\s+|//[^\n]*|/\*.*?\*/', '', code)

    while code:
        print(code)
        match = None
        for token, pattern in tokens:
            regex = re.compile('^' + pattern)
            match = regex.match(code)
            if match:
                lexeme = match.group(0)
                tokens_found.append((token, lexeme))
                code = code[match.end():]
                break
        if not match:
            raise Exception('Invalid token: ' + code[0])
    
    return tokens_found

def main():
    with open(r'codigo.c', 'r') as file:
        code = file.read()

    tokens = tokenize(code)

    # Imprimindo os tokens reconhecidos
    for i, (token, lexeme) in enumerate(tokens, 1):
        print(f'linha: {i:2}  coluna: {lexeme[0]}  token: {token:15} lexema: {lexeme}')

if __name__ == '__main__':
    main()