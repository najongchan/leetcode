# https://school.programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    for i, citation in enumerate(citations):
        if citation >= i + 1:
            answer = i + 1
        else:
            break

    return answer


print(solution([3, 0, 6, 1, 5]))
