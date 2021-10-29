n = int(input())


def prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


for j in range(1, n):
    if prime(j) is True and prime(n-j) is True:
        print(j, n-j)
