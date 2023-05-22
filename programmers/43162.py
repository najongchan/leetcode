# https://school.programmers.co.kr/learn/courses/30/lessons/43162
def solution(n, computers):
    answer = 0
    visited = [False] * n

    for index in range(n):
        if not visited[index]:
            stack = [index]

            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True
                    for i, j in enumerate(computers[node]):
                        if j == 1 and not visited[i]:
                            stack.append(i)
            answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
