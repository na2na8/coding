def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i, s in enumerate(prices) :
        if not stack or stack[len(stack)-1][1] <= s :
            stack.append((i, s))
        if stack[len(stack)-1][1] > s :
            while stack :
                popped = stack.pop()
                if popped[1] <= s :
                    stack.append(popped)
                    break
                answer[popped[0]] = i-popped[0]
            stack.append((i,s))
    
    for elem in stack :
        answer[elem[0]] = len(prices)-(elem[0] + 1)

    return answer
            


print(solution([1, 2, 3, 2, 3]))
print(solution([3, 2, 1, 5, 4]))
print(solution([1, 2, 3, 2, 3, 3, 2, 1, 5, 4]))