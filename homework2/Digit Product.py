n=int(input())
product=1
while n!=0:
    if((n%10)!=0):
     product=product * (n%10)
    n=n//10
print(product)
