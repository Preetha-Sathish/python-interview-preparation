def nums():
    yield 1
    yield 2
    yield 3
g=nums()
print(next(g))
print(next(g))
print(next(g))
#print(next(g)) #StopIteration

def names(*args):
    for i in args:
        yield i

n = names("sp","preethu","sathish","hardhik")
for name in n:
    print(name)


