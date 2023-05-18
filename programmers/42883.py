# https://school.programmers.co.kr/learn/courses/30/lessons/42883
def solution(number, k):
    stack = []

    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1

        stack.append(num)

    # 만약 k개의 수를 제거하지 못했다면, 남은 수 중에서 뒤에서부터 k개를 제거합니다.
    while k > 0:
        stack.pop()
        k -= 1

    answer = ''.join(stack)
    return answer


print(solution("1924", 2))  # "94"
print(solution("1231234", 3))  # "3234"
print(solution("4177252841", 4))  # "775841"
