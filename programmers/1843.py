# https://school.programmers.co.kr/learn/courses/30/lessons/1843
def solution(arr):
    n = len(arr) // 2 + 1  # 숫자의 개수
    dp_max = [[0] * n for _ in range(n)]  # 최댓값을 저장할 DP 테이블
    dp_min = [[0] * n for _ in range(n)]  # 최솟값을 저장할 DP 테이블

    # 초기화
    for i in range(n):
        dp_max[i][i] = int(arr[i * 2])
        dp_min[i][i] = int(arr[i * 2])

    for d in range(1, n):
        for i in range(n - d):
            j = i + d
            dp_max[i][j] = float('-inf')
            dp_min[i][j] = float('inf')

            for k in range(i, j):
                if arr[k * 2 + 1] == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k + 1][j])
                else:
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k + 1][j])

    return dp_max[0][n - 1]


print(solution(["1", "-", "3", "+", "5", "-", "8"]))
print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))