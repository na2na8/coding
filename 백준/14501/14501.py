
if __name__ == "__main__" :
    # 남은 일자
    N = int(input)
    # 걸리는 시간
    T = []
    # 받는 임금
    P = []
    for n in range(N) :
        T_P = [int(tp) for tp in input().split(' ')]
        T.append(T_P[0])
        P.append(T_P[1])