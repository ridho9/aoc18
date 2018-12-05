def react(polymer):
    string = polymer
    idx = 0
    while idx < len(string) - 1:
        c1, c2 = string[idx], string[idx + 1]
        diff = ord(c1) - ord(c2)

        if diff == 32 or diff == -32:
            # print(idx)
            string = string[:idx] + string[idx + 2:]
            if idx > 0:
                idx -= 1
        else:
            idx += 1
    return string


def filter_polymer(polymer, low_char):
    polymer = filter(lambda x: x != low_char, polymer)
    polymer = filter(lambda x: x != low_char.upper(), polymer)
    return ''.join(polymer)


string = input()

print("p1")
print(len(react(string)))

min_char = 0
min_length = len(string) + 1

print("p2")
for c in range(ord('a'), ord('z') + 1):
    low_char = chr(c)
    result = filter_polymer(string, low_char)
    result = react(result)
    if len(result) < min_length:
        min_char = low_char
        min_length = len(result)
        print(min_char, min_length)
