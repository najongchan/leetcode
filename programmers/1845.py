# https://school.programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    limit = len(nums)/2
    pool = set(nums)

    if len(pool) >= limit:
        return limit
    else:
        return len(pool)
