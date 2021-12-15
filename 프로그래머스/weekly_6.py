def compare(point, set_list, compare_list, plus, mult) :
    for s in set_list :
        if compare_list.count(s) > 1 :
            for p in point :
                if p[0] == s :
                    point[point.index(p)][0] += plus[p[1]]*mult
    return point

def solution(weights, head2head):
    answer = []
    print('---------------------------------------------------------------------------------------------------------------------------')
    win_rate = [0 if h.count('N') == len(weights) else h.count('W')/(h.count('W')+h.count('L')) for h in head2head]
    
    win_weighter = []
    for i, h2h in enumerate(head2head) :
        expt_b_w = weights[:i] + weights[i+1:]
        expt_b_h2h = h2h[:i] + h2h[i+1:]
        win_weighter.append(len([j for j in range(len(expt_b_w)) if expt_b_h2h[j]=='W' and expt_b_w[j]>weights[i]]))
    
    dicts = []
    for i in range(len(weights)) :
        dicts.append({"index": i, "weight" : weights[i], "win_rate" : win_rate[i], "win_weighter" :win_weighter[i]})

    #1. 인덱스로 정렬
    #2. 자신의 몸무게로 정렬
    #3. 무거운 복서를 이긴 순서로 정렬
    #4. 전체 승률로 정렬
    dicts.sort(key= lambda x : x["weight"], reverse=True)
    print(dicts)
    dicts.sort(key= lambda x : x["win_weighter"] , reverse=True)
    print(dicts)
    dicts.sort(key= lambda x : x["win_rate"] , reverse=True)
    print(dicts)


    return [x["index"]+1 for x in dicts]

    # # 1. 전체 승률이 높은 복서의 번호가 앞쪽으로 갑니다
    # point = [[w, i] for i,w in enumerate(win_rate)]
    # point.sort(reverse=True)
    
    # # 2. 승률이 동일한 복서의 번호들 중에서는 자신보다 몸무게가 무거운 복서를 이긴 횟수가 많은 복서의 번호가 앞쪽으로 갑니다.
    # s_wr = list(set(win_rate))
    # point = compare(point, s_wr, win_rate, win_weighter, 10000000)
    # for s in s_wr :
    #     if win_rate.count(s) > 1 :
    #         for p in point :
    #             if p[0] == s :
    #                 point[point.index(p)][0] += win_weighter[p[1]]*1000000
    # point = [[p[0]*100000000000000, p[1]] for p in point]
    # # 3. 자신보다 무거운 복서를 이긴 횟수까지 동일한 복서의 번호들 중에서는 자기 몸무게가 무거운 복서의 번호가 앞쪽으로 갑니다.    
    # compare_p = list(set(list(list(zip(*point))[0])))
    # point = compare(point, compare_p, list(list(zip(*point))[0]), weights, 10000)

    # # 4. 자기 몸무게까지 동일한 복서의 번호들 중에서는 작은 번호가 앞쪽으로 갑니다.
    # compare_w = list(set(list(list(zip(*point))[0])))
    # for cw in compare_w :
    #     if list(list(zip(*point))[0]).count(cw) > 1 :
    #         for p in point :
    #             if p[0] == cw :
    #                 point[point.index(p)][0] += (1000-p[1])
    # point.sort(reverse=True)

    # answer = [p[1]+1 for p in point]
    # print(point)
    # return answer

weight1 = [50,82,75,120]
head2head1 = ["NLWL","WNLL","LWNW","WWLN"]	#[3,4,1,2]
print(solution(weight1, head2head1))
weight2 = [145,92,86]
head2head2 = ["NLW","WNL","LWN"]	#[2,3,1]
print(solution(weight2, head2head2))
weight3 = [60,70,60]
head2head3 = ["NNN","NNN","NNN"]	#[2,1,3]
print(solution(weight3, head2head3))

    # for s in s_wr :
    #     if win_rate.count(s) > 1 :
    #         for p in point :
    #             if p[0] == s :
    #                 point[point.index(p)][0] += win_weighter[p[1]]*1000000

    # for c in compare_p :
    #     if list(list(zip(*point))[0]).count(c) > 1 :
    #         print(c)
    #         for p in point :
    #             if p[0] == c :
    #                 point[point.index(p)][0] += weights[p[1]]*1000

    # dicts = []
    # for i in range(len(weights)) :
    #     dicts.append({"index": i, "weight" : weights[i], "win" : win[i], "win_heavy" :win2heavy[i]})

    # #1. 인덱스로 정렬
    # #2. 자신의 몸무게로 정렬
    # #3. 무거운 복서를 이긴 순서로 정렬
    # #4. 전체 승률로 정렬
    # dicts.sort(key= lambda x : x["weight"], reverse=True)
    # dicts.sort(key= lambda x : x["win_heavy"] , reverse=True)
    # dicts.sort(key= lambda x : x["win"] , reverse=True)


    # return [x["index"]+1 for x in dicts]