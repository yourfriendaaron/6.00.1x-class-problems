def iterPower(base, exp):
    result = base
    if exp == 0:
        return 1
    else:
        while exp > 1:
            result *= base
            exp -= 1
    return result
