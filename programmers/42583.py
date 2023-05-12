# https://school.programmers.co.kr/learn/courses/30/lessons/42583
def solution(bridge_length, weight, truck_weights):
    answer = 0
    weight_sum = 0
    passed_trucks, passing_trucks = [], [0] * bridge_length
    while len(truck_weights) > 0:
        truck = passing_trucks.pop(0)
        if truck != 0:
            passed_trucks.append(truck)
            weight_sum -= truck

        if len(passing_trucks) < bridge_length and truck_weights[0] + weight_sum <= weight:
            passing_trucks.append(truck_weights.pop(0))
            weight_sum += passing_trucks[-1]
        else:
            passing_trucks.append(0)
        answer += 1
    return answer + bridge_length


print(solution(2, 10, [7, 4, 5, 6]))
