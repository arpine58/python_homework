a=int(input())
b=int(input())
c=int(input())
if(a+b>c and b+c>a and a+c>b):
 if(c<a):
     temp=c
     c=a
     a=temp
 if(c<b):
     temp=c
     c=b
     b=temp
 if(c*c==a*a+b*b):
  print("right")
 if(c*c>a*a+b*b):
  print("obtuse")
 if(c*c<a*a+b*b):
  print("acute")
else:
    print("no triangle")

 



