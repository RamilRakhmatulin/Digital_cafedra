def find_max(*args):
    max=args[0]
    for i in range(1, len(args)):
        if max<args[i]:
            max=args[i]
    return max

print(find_max(5, 3, 8, 10, 3))