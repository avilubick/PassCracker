import hashlib
numtry = 0
passnum = 0
with open("INSERT REF. FILE", "r") as file:
    content = file.read()
    words = content.split()

with open("INSERT PASSLIST", "r") as file:
    content = file.read()
    userpass = content.split()

for x in userpass:
    for y in words:
        p = hashlib.md5(bytes(y, 'utf-8')).hexdigest()
        #print(str(numtry) + ":" + str(passnum))
        print(y)
        numtry = numtry + 1
        if p == x:
            print(str(y) + ": " + str(x))
            with open('INSERT RESULT FILE', 'r'):
                file.write(str(y) + ": " + str(x))
            passnum = passnum + 1



