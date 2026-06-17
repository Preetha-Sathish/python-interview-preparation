a=[1,2,3]
b=a
a.append(4)
print("Reference Example")
print("a =", a)
print("b =", b)

x=[1,2,3]
y=x.copy()
x.append(4)
print("Copy Example")
print("x =", x)
print("y =", y)
