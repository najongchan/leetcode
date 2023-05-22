# https://school.programmers.co.kr/learn/courses/30/lessons/43164
from collections import defaultdict
def solution(tickets):
    r = defaultdict(list)
    for i,j in tickets:
        r[i].append(j)
    for i in r.keys():
        r[i].sort()

    s = ["ICN"]
    p = []
    print(r)
    while s:
        q = s[-1]
        print(q, r[q])

        if r[q] != []:
            s.append(r[q].pop(0))
        else:
            p.append(s.pop())
        print(s)
        print(p)
        print("###lop###")
    return p[::-1]



print(solution([["ICN", "JFK"], ["ICN", "AAD"], ["JFK", "ICN"]]))
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))  # ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"],
                ["ATL", "SFO"]]))  # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
