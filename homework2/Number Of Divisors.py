x=int(input())
count=0
y=1
while y*y<x:
    if(x%y==0):
     count=count+1
    y= y + 1
print(count)