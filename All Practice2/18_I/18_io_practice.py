def great():
    return 5000000000

score = great()
with open("file.txt") as f:
    a = int(f.read())

if a<score:
    with open("file.txt","w") as f:
        f.write(str(score))

