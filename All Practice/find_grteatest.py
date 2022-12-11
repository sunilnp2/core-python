a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
d  = int(input("Enter fourth number : "))

if (a>b and a>c and a>d):
    print(f"The number {a} is greatest !")

elif (b>c and b>d and b>a):
    print(f"the number {b} is greatest!")

elif (c>d and c>a and c>b):
    print(f"The number {c} is greatest!")

else:
    print(f"The Number {d} is greatest!")
