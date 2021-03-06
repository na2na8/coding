

if __name__ == "__main__" :
    # 종이 크기
    N_M = [int(nm) for nm in input().split(' ')]
    N = N_M[0]
    M = N_M[1]

    # 종이
    paper = []
    for n in range(N) :
        row = [int(r) for r in input().split(' ')]
        paper.append(row)
    
    shape = [
        ((0,0),(0,1),(0,2),(0,3)),
        ((0,0),(1,0),(2,0),(3,0)),
        ((0,0),(0,1),(1,0),(1,1)),
        ((0,0),(0,1),(-1,1),(0,2)),
        ((0,0),(1,0),(1,-1),(2,0)),
        ((0,0),(1,0),(1,1),(2,0)),
        ((0,0),(0,1),(1,1),(0,2)),
        ((0,0),(0,1),(0,2),(1,2)), # ㄱ
        ((0,0),(0,1),(0,2),(-1,2)), # ㄱ 위로 뒤집은 것
        ((0,0),(1,0),(1,1),(1,2)), # ㄴ
        ((0,0),(-1,0),(-1,1),(-1,2)), # ㄴ 위로 뒤집은 것
        ((0,0),(1,0),(2,0),(2,1)),
        ((0,0),(1,0),(2,0),(2,-1)),
        ((0,0),(0,1),(1,1),(2,1)),
        ((0,0),(0,1),(1,0),(2,0)),
        ((0,0),(1,0),(0,1),(-1,1)),
        ((0,0),(1,0),(1,1),(2,1)),
        ((0,0),(0,1),(1,1),(1,2)),
        ((0,0),(0,1),(-1,1),(-1,2))
    ]

    max_sum = 0
    for n in range(N) :
        for m in range(M) :
            for s in shape :
                sum_ = 0
                try :
                    for i in range(4) :
                        sum_ += paper[n+s[i][0]][m+s[i][1]]
                    if sum_ > max_sum :
                        max_sum = sum_
                except IndexError :
                    continue
        
    
    print(max_sum)
