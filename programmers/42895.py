# https://school.programmers.co.kr/learn/courses/30/lessons/42895
def solution(N, number):
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        if number in dp[i]:
            return i

    for i in range(2, 9):
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(y - x)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)
                    if x != 0:
                        dp[i].add(y // x)
        print(dp)
        if number in dp[i] and i <= 8:
            return i

    return -1


print(solution(5, 12))
print(solution(5, 31168))
