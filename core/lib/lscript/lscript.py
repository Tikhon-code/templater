from lib.lscript.lexer import split_lines
from lib.lscript.parser import parse_lines
from lib.lscript.interp import execute_lines

def read(file):
    with open(file, "r") as f:
        return f.readlines()

def write(file, code):
    with open(file, "w") as f:
        f.write(code)

def run(file):
    try:
        content = read(file)
    except FileNotFoundError:
        print(f"{file}: File not found.")
        return

    try:
        lexed_all = split_lines(content)
    except Exception as e:
        print(f"ERR in split: {e}")
        return

    try:
        parsed_all = parse_lines(lexed_all)
    except Exception as e:
        print(f"ERR on parsed: {e}")
        return

    try:
        execute_lines(parsed_all)
    except Exception as e:
        print(f"ERR on execute: {e}")
        return
