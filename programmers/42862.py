# https://school.programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    lost.sort(reverse=True)
    reserve.sort(reverse=True)

    for i in lost[:]:
        if i in reserve[:]:
            reserve.remove(i)
            lost.remove(i)

    for j in lost[:]:
        if j - 1 in reserve:
            lost.remove(j)
            reserve.remove(j-1)
        elif j + 1 in reserve:
            lost.remove(j)
            reserve.remove(j+1)

    return n - len(lost)


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [4, 5], [3, 4]))

