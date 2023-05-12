# https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = [arr.pop(0)]
    for num in arr:
        if answer[-1] != num:
            answer.append(num)
    return answer