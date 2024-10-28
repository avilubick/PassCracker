import hashlib

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', ':', ';', "'", '.', '/', '?', '-', '=']

hash = '3f9618923e935a06ccef7c9c7535f7bc'

for first in a:
    for second in a:
        for third in a:
            for fourth in a:
                ans = first+second+third+fourth
                x = hashlib.md5(bytes(ans, 'utf-8')).hexdigest()
                print(ans)
                if x == hash:
                    print(ans)
                    exit()

