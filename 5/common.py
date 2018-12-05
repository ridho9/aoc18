def react(string):
    idx = 0
    while idx < len(string) - 1:
        c1, c2 = string[idx], string[idx + 1]
        if ord(c1) ^ ord(c2) == 32:
            string = string[:idx] + string[idx + 2:]
            if idx > 0:
                idx -= 1
        else:
            idx += 1
    return string
