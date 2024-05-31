def outer(a):
    print("Outer: {}".format(a))

    def inner():
        print("\tInner: {}".format(a))

    return inner

test = outer('test')

del outer

test()
