# https://school.programmers.co.kr/learn/courses/30/lessons/42584
def solution(prices):
    answer = [0] * len(prices)
    stack = [[0, prices[0]]]

    for i in range(1, len(prices)):
        while stack and stack[-1][1] > prices[i]:
            prev = stack.pop()[0]
            answer[prev] = i - prev
        stack.append([i, prices[i]])

    for idx, val in stack:
        answer[idx] = len(prices) - idx - 1

    return answer

print(solution([1, 2, 3, 1, 3]))
