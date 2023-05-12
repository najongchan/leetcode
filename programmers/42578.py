# https://school.programmers.co.kr/learn/courses/30/lessons/42578
from collections import defaultdict
def solution(clothes):
    closet = defaultdict(list)
    for cloth in clothes:
        closet[cloth[1]].append(cloth[0])

    answer = 1
    for v in closet.values():
        answer *= (len(v) + 1)
    answer -= 1
    return answer