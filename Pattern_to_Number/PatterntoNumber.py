Pattern = "GACGTAAGGCGCCTCAA"

def PatterntoNumber(Pattern):
    result = 0

    for a, b in enumerate(Pattern):
        if b == "A":
            result = result + 0 * 4 ** (len(Pattern) - 1 - a)
        elif b == "C":
            result = result + 1 * 4 ** (len(Pattern) - 1 - a)
        elif b == "G":
            result = result + 2 * 4 ** (len(Pattern) - 1 - a)
        elif b == "T":
            result = result + 3 * 4 ** (len(Pattern) - 1 - a)
    return result
print(PatterntoNumber(Pattern))
