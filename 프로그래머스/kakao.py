def solution(v):
    answer = [0,0]
    X = {}
    Y = {}
    for V in v :
        if V[0] not in list(X.keys()) :
            X[V[0]] = 1
        else :
            X[V[0]] += 1
        
        if V[1] not in list(Y.keys()) :
            Y[V[1]] = 1
        else :
            Y[V[1]] += 1
    
    x_keys = list(X.keys())
    y_keys = list(Y.keys())
    for i in range(2) :
        if X[x_keys[i]] == 1 :
            answer[0] = x_keys[i]
        if Y[y_keys[i]] == 1 :
            answer[1] = y_keys[i]
        
        

    print('Hello Python')

    return answer