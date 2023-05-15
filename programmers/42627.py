# https://school.programmers.co.kr/learn/courses/30/lessons/42627
def solution(jobs):
    jobs.sort()
    temp = []
    for i in range(len(jobs)):
        if jobs[i][0] == 0:
            temp.append(jobs[i])
    temp.sort(key=lambda x: x[1])

    jobs = temp + jobs[len(temp):]
    answer = 0
    tic = 0
    n = len(jobs)

    while jobs:
        if jobs[0][0] > tic:
            tic = jobs[0][0]
        else:
            job = jobs.pop(0)
            answer += job[1] + tic - job[0]
            tic += job[1]

            candidate_jobs = []
            for i in range(len(jobs)):
                if tic >= jobs[i][0]:
                    candidate_jobs.append(jobs[i])
            candidate_jobs.sort(key=lambda x: x[1])
            jobs = candidate_jobs + jobs[len(candidate_jobs):]

    return answer // n


print(solution([[0, 3], [2, 6], [1, 9]]))
