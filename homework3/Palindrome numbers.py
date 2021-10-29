a = int(input())
b = int(input())


def palindrome(x):
    temp = x
    rev = 0
    while x > 0:
        dig = x % 10
        rev = rev*10+dig
        x = x//10
    if temp == rev:
        return True
    else:
        return False


for i in range(a, b):
    if palindrome(i) is True:
     print(i)
