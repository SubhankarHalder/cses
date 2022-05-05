def solution(num):
    for val in range(1, num+1):
        place_knights = (val**2)*(val**2-1)//2
        attack_positions = 4*(val-1)*(val-2)
        non_attack_pos = place_knights-attack_positions
        print(non_attack_pos)


if __name__ == "__main__":
    n = int(input())
    solution(n)
