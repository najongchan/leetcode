# https://school.programmers.co.kr/learn/courses/30/lessons/42897
def solution(money):
    n = len(money)
    dp1 = [0] * n  # 첫 번째 집을 털었을 경우의 DP 테이블
    dp2 = [0] * n  # 첫 번째 집을 털지 않았을 경우의 DP 테이블

    # 첫 번째 집을 털었을 경우
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-2] + money[i], dp1[i-1])

    # 첫 번째 집을 털지 않았을 경우
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i-2] + money[i], dp2[i-1])

    # 마지막 집을 기준으로 두 가지 경우 중 더 큰 값 반환
    return max(dp1[n-2], dp2[n-1])


print(solution([1, 2, 3, 1]))
