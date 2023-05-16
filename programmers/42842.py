# https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    total_tiles = brown + yellow
    for i in range(1, int(total_tiles**0.5) + 1):
        if total_tiles % i == 0:
            width = total_tiles // i
            height = i
            if (width - 2) * (height - 2) == yellow:
                return [width, height]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
