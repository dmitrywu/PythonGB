def sum_str(*args):
    res = ""
    for i in args:
        res += i
    return res


print(sum_str("q", "e", "l", "a", "s"))
