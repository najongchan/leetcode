# https://school.programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations


def solution(k, dungeons):
    plans = list(permutations(dungeons, len(dungeons)))
    print(plans)

    answer = 0
    for plan in plans:
        possible = 0
        stamina = k
        for dungeon in plan:
            if stamina < dungeon[0] or stamina < dungeon[1]:
                break
            possible += 1
            stamina -= dungeon[1]
        answer = max(answer, possible)
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
