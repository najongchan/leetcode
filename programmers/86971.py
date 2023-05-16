# https://school.programmers.co.kr/learn/courses/30/lessons/86971
def solution(n, wires):
    graph = [[] for _ in range(n + 1)]  # 그래프 초기화
    for v1, v2 in wires:
        graph[v1].append(v2)  # 양방향 그래프 생성
        graph[v2].append(v1)

    answer = float('inf')  # 최소 차이값을 저장할 변수

    def dfs(v, parent):
        nonlocal answer
        count = 1  # 현재 노드를 포함한 송전탑 개수
        for u in graph[v]:
            if u != parent:
                count += dfs(u, v)  # 자식 노드까지의 송전탑 개수를 재귀적으로 계산
        diff = abs(n - 2 * count)  # 두 전력망의 송전탑 개수 차이 계산
        answer = min(answer, diff)  # 최소 차이값 업데이트
        return count

    dfs(1, 0)  # 루트 노드부터 탐색 시작

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
