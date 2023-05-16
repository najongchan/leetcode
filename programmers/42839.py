# https://school.programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    combinations = []
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        for perm in perms:
            num = int(''.join(perm))
            if is_prime(num) and num not in combinations:
                combinations.append(num)
    return len(combinations)


print(solution("17"))
print(solution("110"))
print(solution("011"))

