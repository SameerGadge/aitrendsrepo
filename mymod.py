def countLines(name):
    f = open(name, "r")
    lines = f.readlines()
    f.close()
    return len(lines)

def countChars(name):
    f = open(name, "r")
    chars = f.read()
    f.close()
    return len(chars)

def test(name):
    lines = countLines(name)
    chars = countChars(name)
    print(f"No. of Lines: {lines}, No. of Characters: {chars}")