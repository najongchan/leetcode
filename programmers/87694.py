# https://school.programmers.co.kr/learn/courses/30/lessons/87694
def solution(rectangle, characterX, characterY, itemX, itemY):
    candy = set()
    for x, y, X, Y in rectangle:
        candy.update([(j + 0.5, i) for j in range(y, Y) for i in (x, X)])
        candy.update([(j, i + 0.5) for i in range(x, X) for j in (y, Y)])
    print(candy)
    edge = set()
    for b, a in candy:
        for x, y, X, Y in rectangle:
            if x < a < X and y < b < Y:
                break
        else:
            edge.add((b, a))
    print(edge)
    answer = 0
    return answer


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
