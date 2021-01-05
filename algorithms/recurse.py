def recurse(num):
    if num > 100:
        return
    num += 10
    print(num)
    recurse(num)

recurse(0)
