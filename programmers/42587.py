# https://school.programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    answer = 0
    while True:
        task = priorities.pop(0)
        location -= 1
        print(priorities)
        print(location)

        if priorities and task < max(priorities):
            priorities.append(task)
            if location < 0:
                location = len(priorities) - 1
        else:
            answer += 1

        if location < 0:
            return answer


print(solution([2, 1, 3, 2], 2))
