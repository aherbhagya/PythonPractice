import string
alpha = string.ascii_lowercase

n = int(input())
L = []

for i in range(n):
    s = "-".join(alpha[i:n])
    print(s)
    L.append(s[::-1]+s[1:])
    print(L)

width = len(L[0])
print("//")
for i in range(n-1, 0, -1):
    print(L[i].center(width, "-"))

for i in range(n):
    print(L[i].center(width, "-"))
    
print("################################################")
size = int(input())
alphabet = string.ascii_lowercase

for i in range(size - 1, 0, -1):
    row = ["-"] * (size * 2 - 1)
    for j in range(0, size - i):
        row[size - 1 - j] = alphabet[j + i]
        row[size - 1 + j] = alphabet[j + i]
    print("-".join(row))

for i in range(0, size):
    row = ["-"] * (size * 2 - 1)
    for j in range(0, size - i):
        row[size - 1 - j] = alphabet[j + i]
        row[size - 1 + j] = alphabet[j + i]
    print("-".join(row))