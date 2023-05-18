# https://school.programmers.co.kr/learn/courses/30/lessons/42861
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, costs):
    parent = [num for num in range(n)]
    costs.sort(key=lambda x: x[2])
    print(parent)
    print(costs)
    answer = 0

    for i, j, cost in costs:
        if find(parent, i) != find(parent, j):
            union(parent, i, j)
            answer += cost

    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
