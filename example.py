import hashlib
#with open("C:\\Users\\avilu\Downloads\\rockyou (1).txt", "r") as file:
with open("C:\\Users\\avilu\\Downloads\\10-million-password-list-top-1000000.txt", "r") as file:
    content = file.read()
    words = content.split()

with open("C:\\Users\\avilu\\Downloads\\SHA1.txt", "r") as file:
    content = file.read()
    userpass = content.split()


dict1 = {}
for x in words:
    p = hashlib.md5(bytes(x, 'utf-8')).hexdigest()
    dict1[p] = x





for i in userpass:
    print(i)
    for z in dict1:
        if z == i:
            print(i + z)
            exit()
        print(z + " " + i)
    print("not found")

