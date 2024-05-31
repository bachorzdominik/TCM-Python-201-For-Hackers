def gen_demo():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n

test = gen_demo()
print(test)

print(next(test))
print(next(test))
print(next(test))
# print(next(test)) # StopIteration
print('---')

test2 = gen_demo()
for i in test2:
    print(i)
