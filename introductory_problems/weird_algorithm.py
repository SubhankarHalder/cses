def solution(n):
    res = []
    res.append(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            res.append(n)
        else:
            n = 3*n + 1
            res.append(n)
    print(*res)


if __name__ == "__main__":
    n = int(input())
    solution(n)            
