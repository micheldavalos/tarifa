x = int(input())
n = int(input())

i = 0
trans = 0
while i < n:
    p = int(input())
    trans = x - p + trans
    i += 1
print(x + trans)