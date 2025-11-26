def split(code):
    lecode = len(code)

    all = []
    current = []

    is_string = False
    string_char = ""

    pos = 0

    while pos < lecode:
        c = code[pos]
        pos += 1
        
        if c == string_char:
            if current:
                current.append(c)
                all.append(''.join(current))
                current = []
        
            is_string = False
            string_char = ""

            continue

        if not is_string:
            if c in (";", ":"):
                if current:
                    all.append(''.join(current))
                    current = []

                all.append(c)

                continue    
        
            if c in ("'", '"'):
                if current:
                    all.append(''.join(current))
                    current = []

                is_string = True
                string_char = c

            if c == " ":
                if current:
                    all.append(''.join(current))
                    current = []

                continue
                    
        current.append(c)

    if current:
        all.append(''.join(current))

    return all


def split_lines(code):
    all = []

    for line in code:
        line = line.strip()

        if line:
            all.append(split(line))

    return all
