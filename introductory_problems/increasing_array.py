def solution(n, arr):
    temp = None
    res = 0
    for idx, val in enumerate(arr):
        if idx != 0 and val < temp:
            res += temp-val
        else:
            temp = val
    print(res)


if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().split()]
    solution(n, arr)
