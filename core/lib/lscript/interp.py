import os

def execute(parsed):
    if parsed["op"] == "CALL":
        func, *args = parsed["args"]

        if func == "mkdir":
            for arg in args:
                os.makedirs(arg)

        elif func == "touch":
            for arg in args:
                with open(arg, "w"): pass

        elif func == "cd":
            for arg in args:
                os.chdir(arg)

        else:
            return 1, func
        
def execute_lines(code):
    for line, parsed in enumerate(code):
        ret = execute(parsed[-1])

        if ret:
            if ret[0] == 1:
                print(f"[line {line+1}] {ret[1]}: Func not defined")
