n = int(input())
a = []
b = list()
for i in range(0, n): 
    e = int(input()) 
    a.append(e)
b.append(sum(a))
for i in range(1, len(a)):
    b.append(b[i-1]-a[i-1])
print(b)
