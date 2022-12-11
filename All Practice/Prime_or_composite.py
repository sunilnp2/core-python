n = int(input("Enter what do you wnat to check :"))
prime = False
for i in range(2, n):
    if(n%i == 0):
        prime  = True

if prime:
    print("This is Prime Number")

else:
    print("This is compite Number")