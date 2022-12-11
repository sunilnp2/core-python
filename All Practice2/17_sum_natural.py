def sum(n):
    sum = 0
    for i in range(n):
        sum = sum + i
        return sum

n = int(input("Enter a natural Number:\n"))
s = sum(n)
print(s)
