# https://school.programmers.co.kr/learn/courses/30/lessons/42628
from collections import deque


def solution(operations):
    answer = deque()
    for operation in operations:
        input_data = operation.split(' ')

        if input_data[0] == 'I':
            answer.append(int(input_data[1]))
        elif len(answer) > 0 and input_data[0] == 'D':
            if int(input_data[1]) > 0:
                answer.remove(max(answer))
            else:
                answer.remove(min(answer))

    if len(answer) == 0:
        return [0, 0]
    return [max(answer), min(answer)]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))