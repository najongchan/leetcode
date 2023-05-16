# https://school.programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    width, height = 0, 0

    for size in sizes:
        w, h = size[0], size[1]
        if h > w:
            h, w = w, h
        width = max(w, width)
        height = max(h, height)
    return height * width


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
