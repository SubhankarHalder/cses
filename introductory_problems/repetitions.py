def solution(s):
    temp = 'x'
    count = 0
    res = 0
    for val in s:
        if val == temp:
            count += 1
        else:
            count = 1
        res = max(res, count)
        temp = val
    print(res)


if __name__ == "__main__":
    s = input()
    solution(s)
