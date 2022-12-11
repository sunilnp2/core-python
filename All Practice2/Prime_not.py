a = int(input("Enter a number :\n"))
is_prime = True
for i in range(2,a):
    if (a % i == 0):
        is_prime = False
        
if is_prime:
        print("This is prime number")

else:
        print("this is composite number")

