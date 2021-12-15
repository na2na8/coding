def solution(bridge_length, weight, truck_weights):
    in_bridge = []
    in_bridge_distance = []
    trucks = len(truck_weights)
    done = []

    sec = 0
    while len(done) != trucks :
        if in_bridge_distance and in_bridge_distance[0] == bridge_length :
            in_bridge_distance = in_bridge_distance[1:]
            done.append(in_bridge[0])
            in_bridge = in_bridge[1:]
        if truck_weights and sum(in_bridge) + truck_weights[0] <= weight :
            in_bridge.append(truck_weights[0])
            in_bridge_distance.append(0)
            truck_weights = truck_weights[1:]
        
        in_bridge_distance = [d+1 for d in in_bridge_distance]
        sec += 1

    return sec

# print(truck_weights, in_bridge, in_bridge_distance, done)
print(solution(2, 10, [7,4,5,6]))
print("-------------------------------------------------------")
print(solution(100, 100, [10]))
print("-------------------------------------------------------")
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
