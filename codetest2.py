def solution(bishops):
    answer = 0

    x_map = {
        'A': '0','B': '1','C': '2','D': '3','E': '4','F': '5','G': '6','H': '7',
    }
    table = [[0 for _ in range(8)] for _ in range(8)]
    for mal in bishops:
        x = int(x_map[mal[0]])
        y = int(mal[1]) - 1
        
        table[y][x] += 1
        t1 = [y, x]
        t2 = [y, x]
        t3 = [y, x]
        t4 = [y, x]

        for _ in range(7):
            t1[0] = t1[0] + 1
            t1[1] = t1[1] - 1

            t2[0] = t2[0] - 1
            t2[1] = t2[1] + 1

            t3[0] = t3[0] + 1
            t3[1] = t3[1] + 1

            t4[0] = t4[0] - 1
            t4[1] = t4[1] - 1

            if t1[0] < 8 and t1[1] > -1:
                table[t1[0]][t1[1]] += 1

            if t2[0] > -1 and t2[1] < 8:
                table[t2[0]][t2[1]] += 1
           
            if t3[0] < 8 and t3[1] < 8:
                table[t3[0]][t3[1]] += 1
            
            if t4[0] > -1 and t4[1] > -1:
                table[t4[0]][t4[1]] += 1

        # for x in range(7, -1, -1):
        #     print(table[x])
        # print('\n')
    for i in range(8):
        answer += table[i].count(0)

    return answer



input1 = ["D5"]
print(solution(input1))
