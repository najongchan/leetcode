# https://school.programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    n = len(answers)
    student_1 = ([1, 2, 3, 4, 5] * (n // 5 + 1))[:n]
    student_2 = ([2, 1, 2, 3, 2, 4, 2, 5] * (n // 8 + 1))[:n]
    student_3 = ([3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (n // 10 + 1))[:n]

    score_board = {
        1: 0,
        2: 0,
        3: 0,
    }

    for i in range(n):
        if answers[i] == student_1[i]:
            score_board[1] += 1
        if answers[i] == student_2[i]:
            score_board[2] += 1
        if answers[i] == student_3[i]:
            score_board[3] += 1

    return [k for k, v in score_board.items() if max(score_board.values()) == v]


print(solution([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2]))
print(solution([1, 3, 2, 4, 2]))
