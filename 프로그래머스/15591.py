# https://www.acmicpc.net/problem/15591
# 1 <= N <= 5000, 1<= Q <= 5000
# 1 ≤ ki ≤ 1,000,000,000, 1 ≤ vi ≤ N
import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

def getMin(a, b) :
    if a < b and a > 0 :
        return a
    elif a > b and b > 0 :
        return b
    else :
        return a

    

def getMinGraph(graph, N) :
    for i, g in enumerate(graph) :
        for j, elem in enumerate(g[i+1:]) :
            # print(elem)
            num = i + j + 1
            if elem != 0 :
                for u in range(N) :
                    if u != i and u != num :
                        min_ = getMin(elem[0], graph[num][u][0])
                        # print(i, num, u, min_)
                        if graph[u][num][1] == False :
                            graph[u][num][0] = min_
                            graph[u][num][1] = True
                        if graph[num][u][1] == False :
                            graph[num][u][0] = min_
                            graph[num][u][1] = True
                        print(min_, u, num)
                        pp.pprint(graph)

    return graph
                



def main() :
    N_Q = input().split(' ')
    # N : 동영상 개수 | Q : 농부의 질분 갯수
    N, Q = int(N_Q[0]), int(N_Q[1])

    graph = [[[0, False] for i in range(N)] for _ in range(N)]
    for n in range(N-1) :
        p_q_r = input().split(' ')
        p, q, r = int(p_q_r[0]), int(p_q_r[1]), int(p_q_r[2])
        graph[p-1][q-1] = [r, True]
        graph[q-1][p-1] = [r, True]
    for i in range(N) :
        graph[i][i][1] = True
    pp.pprint(graph)
    graph = getMinGraph(graph, N)
    
    pp.pprint(graph)
    ans = []
    for q in range(Q) :
        k_v = input().split(' ')
        k, v = int(k_v[0]), int(k_v[1])
        # k 임계값, v = 동영상(기준)
        count = 0
        for USADO in graph[v-1] :
            if USADO[0] >= k :
                count+=1
        ans.append(count)
    
    for a in ans :
        print(a)
    
main()