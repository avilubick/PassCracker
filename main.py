import hashlib
numtry = 0
passnum = 0
with open("C:\\Users\\avilu\\Downloads\\10-million-password-list-top-1000000.txt", "r") as file:
    content = file.read()
    words = content.split()

with open("C:\\Users\\avilu\\Downloads\\SHA1.txt", "r") as file:
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
            with open('C:\\Users\\avilu\\PycharmProjects\\idk\\found', 'r'):
                file.write(str(y) + ": " + str(x))
            passnum = passnum + 1



