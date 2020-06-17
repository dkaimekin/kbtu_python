l = int(input())
r = int(input())

for i in range(l, r+1):
    if i % 7 == 1 or i % 7 == 2 or i % 7 == 5:
        print(i)
