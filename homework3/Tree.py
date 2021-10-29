def tree(n):
    for i in range(1, n + 1, 2):
        j = (n - i) // 2
        print(" " * j, "*" * i)


n = int(input())
tree(n)
