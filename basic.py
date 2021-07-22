def foo(*args):
    print(type(args))
    args = [x.upper() for x in args]
    print(type(args))
    return sorted(args)
