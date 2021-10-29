n=int(input())
sum=0
while n>=10:
 while(n!=0):
     sum=sum+(n%10)
     n=n//10
 print(sum)
 n=sum
 sum=0



