t = int(input())

for _ in range(t):
    n = int(input())

    k = 1
    x = n

    i = 2

    while i * i <= x:
        if x % i == 0:
            k *= i

            while x % i == 0:
                x //= i

        i += 1

    if x > 1:
        k *= x

    print(k)
