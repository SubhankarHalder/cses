def solution(n, arr):
    n_sum = (n * (n+1))//2
    for val in arr:
        n_sum -= val
    print(n_sum)


if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().split()]
    solution(n, arr)
