from common import react


def filter_polymer(polymer, low_char):
    def f(x):
        return (x != low_char) and (x != low_char.upper())
    polymer = filter(f, polymer)
    return ''.join(polymer)


string = input()
min_length = len(string) + 1

for c in range(ord('a'), ord('z') + 1):
    low_char = chr(c)
    result = filter_polymer(string, low_char)
    result = react(result)
    if len(result) < min_length:
        min_length = len(result)
        print(low_char, min_length)
