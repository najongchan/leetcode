# https://school.programmers.co.kr/learn/courses/30/lessons/84512
from itertools import product


def solution(word):
    moum = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    for i in range(len(moum)):
        dictionary += list(''.join(p) for p in product(moum, repeat=i + 1))

    dictionary.sort()
    print(dictionary)
    return dictionary.index(word) + 1


print(solution('A'))
