def deco(a):
    print("Hello Deco1")
    a()
    print("Deco2")

def func():
    print("This is decorator function")


deco(func)