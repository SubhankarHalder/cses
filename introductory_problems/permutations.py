def solution(n):
    if n == 1:
        print("1")
    elif n == 4:
        print("2 4 1 3")
    elif n < 4:
        print("NO SOLUTION")
    else:
        right = n
        left = n-1
        res = []
        while len(res) != n:
            while right > 0:
                res.append(right)
                right -= 2
            while left > 0:
                res.append(left)
                left -= 2
        print(*res)
            

if __name__ == "__main__":
    n = int(input())
    solution(n)
