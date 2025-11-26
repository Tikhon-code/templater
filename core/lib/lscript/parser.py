def parse(code):
    lecode = len(code)

    parsed = []

    to_args = 0

    pos = 0

    while pos < lecode:
        t = code[pos]
        pos += 1

        if parsed:
            cparsed = parsed[-1]
        else:
            cparsed = parsed

        if to_args > 0:
              for _ in range(to_args):
                cparsed = cparsed["args"]

        if pos < lecode:
            if code[pos] == ":":
                parsed.append({"op": "CALL", "args": [t]})
                pos += 1
                to_args += 1
                continue

        cparsed.append(t)

    return parsed


def parse_lines(code):
    parsed = []

    for line in code:
        if line:
            parsed.append(parse(line))

    return parsed
