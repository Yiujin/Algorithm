def solution(bridge_length, weight, truck_weights): # 다시 풀기
    answer = 0
    in_bridge = [0] * bridge_length

    if sum(truck_weights) <= weight and len(truck_weights) <= bridge_length:
        return bridge_length + len(truck_weights)

    while truck_weights:
        print(f'in_bridge : {in_bridge}')
        del in_bridge[0]
        print(f'in_bridge after del : {in_bridge}, remain truck : {truck_weights}')
        if sum(in_bridge) + truck_weights[0] <= weight: 
            in_bridge.append(truck_weights.pop(0))
        else:
            in_bridge.append(0)

        answer += 1
    answer += len(in_bridge)

    return answer



if __name__ == "__main__":
    bridge_length, weight, truck_weights = 2, 10,[7,4,5,6] # 8
    bridge_length2, weight2, truck_weights2 = 100, 100, [10] # 101
    bridge_length3, weight3, truck_weights3 = 100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10] # 110
    bridge_length4, weight4, truck_weights4 = 3, 10,[7,2,5,6] # 11


    print('answer : ',solution(bridge_length, weight, truck_weights))
    print('answer : ',solution(bridge_length2, weight2, truck_weights2))
    print('answer : ',solution(bridge_length3, weight3, truck_weights3))
    print('answer : ',solution(bridge_length4, weight4, truck_weights4))
