# https://school.programmers.co.kr/learn/courses/30/lessons/42746
import functools

def solution(numbers):
    # numbers를 문자열로 변환
    numbers = list(map(str, numbers))

    # 비교 함수 정의
    def compare(x, y):
        if int(x + y) > int(y + x):
            return -1
        elif int(x + y) < int(y + x):
            return 1
        else:
            return 0

    # 비교 함수를 사용하여 numbers 정렬
    numbers.sort(key=functools.cmp_to_key(compare))

    # 정렬된 numbers를 문자열로 이어붙임
    answer = ''.join(numbers)

    # answer가 0으로만 구성되어 있는 경우, 답은 '0'
    if answer[0] == '0':
        return '0'

    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
