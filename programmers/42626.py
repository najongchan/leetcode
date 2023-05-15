# https://school.programmers.co.kr/learn/courses/30/lessons/42626
import heapq


def solution(scoville: list[int], K: int):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) > 1 and scoville[0] < K:
        answer += 1
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)

    if scoville and scoville[0] < K:
        return -1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
