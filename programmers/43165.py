# https://school.programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    answer = 0

    def dfs(index, result):
        nonlocal answer

        if index == len(numbers):
            if result == target:
                answer += 1
            return

        dfs(index + 1, result + numbers[index])
        dfs(index + 1, result - numbers[index])
    dfs(0, 0)

    return answer


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
