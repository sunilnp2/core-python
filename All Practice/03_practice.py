# my_list = []
# sum = 0
# for i in range(1,3):
   
#     a = int(input("Enter Number a :"))
#     # sum = sum + a
#     sum += a
#     my_list.append(a)
# print(my_list)
# print(sum)

# dict = {}

# n = int(input("How many dictionary you want :"))

# for i in range(n):
#     d_key = input("Enter key : ")
#     d_value = input("Enter value : ")
     
#     dict[d_key] = d_value

# print(dict)



def si():
    p = int(input("Enter p : "))
    t = float(input("Enter t : "))
    r = float(input("Enter r : "))
    si = p*t*r/100
    print(si)

    y = int(input("Enter 1 for again :"))
    if y == 1:
        si()

print(si())











