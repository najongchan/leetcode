# https://school.programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    people.sort()
    answer = 0
    left, right = 0, len(people) - 1
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        answer += 1

    return answer


print(solution([70, 50, 80, 50], 100))
