def mylist(*args):
    l = []
    if args:
        for item in args:
            l.append(item)
    print(l)
mylist("Sunil", 5, "anil")


    