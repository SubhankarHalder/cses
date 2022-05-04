def add(p_num, slide):
    pf_sq = (p_num-1)*(p_num-1)
    return pf_sq + slide


def subtract(p_num, slide):
    pf_sq = (p_num)*(p_num)
    return pf_sq - slide + 1


def solution(x, y):
    if y >= x:
        if y % 2 == 0:
            return add(y, x)
        else:
            return subtract(y, x)
    else:
        if x % 2 == 0:
            return subtract(x, y)
        else:
            return add(x, y)


if __name__ == "__main__":
    n = int(input())
    arr = []
    for idx in range(n):
        x, y = [int(x) for x in input().split()]
        arr.append((x, y))
    for val in arr:
        print(solution(val[0], val[1]))
