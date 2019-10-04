def solution(sticker):
    answer = 0


    sticker.append(0)
    sticker.insert(0, 0)
    while sticker.count(0) < len(sticker):
        max_value = max(sticker)
        max_index = sticker.index(max_value)
        if max_value < (sticker[max_index-1] + sticker[max_index+1]):
            sticker[max_index] = 0
        else:
            answer += max_value
            sticker[max_index-1] = 0
            sticker[max_index+1] = 0
            sticker[max_index] = 0
    
    return answer



input1 = [12, 80, 14, 22, 100]
print(solution(input1))