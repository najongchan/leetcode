def solution(goods, boxes):
    answer = 0

    goods.sort(reverse=True)
    boxes.sort(reverse=True)

    while goods and (goods[0] > boxes[0]):
        del goods[0]

    for good in goods:
        if boxes:
            box = boxes[0]
            if box >= good:
                answer += 1
                del boxes[0]
        
        else:
            break

    return answer



input1 = [10,8,9]
input2 = [5,6,4]
print(solution(input1, input2))
