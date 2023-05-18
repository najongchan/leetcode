# https://school.programmers.co.kr/learn/courses/30/lessons/42860
def solution(name):
    up_down_moves = [min(ord(char) - ord('A'), ord('Z') - ord(char) + 1) for char in name]
    cursor_moves = len(name) - 1

    for i in range(len(name)):
        next_i = i + 1
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        cursor_moves = min(cursor_moves, i + len(name) - next_i + min(i, len(name) - next_i))

    return sum(up_down_moves) + cursor_moves

print(solution('JAN'))
