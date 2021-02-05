def xor(a, b):
    if a and b or not a and not b:
        return False

    if a:
        return a
    else:
        return b
