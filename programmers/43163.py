# https://school.programmers.co.kr/learn/courses/30/lessons/43163
def solution(begin, target, words):
    if target not in words:
        return 0

    answer = 0
    visited = [False] * len(words)
    stack = [begin]

    while stack:
        current = stack.pop()

        for k in range(len(words)):
            count = 0
            for i in range(len(current)):
                if words[k][i] == current[i]:
                    count += 1
            if count == len(current) - 1 and not visited[k]:
                stack.append(words[k])
                visited[k] = True
        answer += 1
        if target in stack:
            break

    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0

