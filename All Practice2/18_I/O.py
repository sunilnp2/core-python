#1)for read data
# f = open('file.txt')
#  data = f.read()
# print(data)
# f.close()

# 2) for write data
# f = open('file.txt','w')
# data = f.write('Hello write this text with clear another text')
# print(data)
# f.close()

# 3) for append data
# f = open('file.txt','a')
# data = f.write('Append this data also here')
# f.close()

# 4) for with way this way you don't need to close a file
with open("file.txt",) as f:
    data  = f.read()
    print(data)