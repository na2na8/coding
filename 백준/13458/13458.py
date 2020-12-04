import math

if __name__ == "__main__" :
    # 시험장 개수
    N = int(input())

    # 각 시험장의 응시자 수
    A = input()
    A_i = [int(a) for a in A.split(' ')]

    # 총감독 감시 가능 인원, 부감독 감시 가능 인원
    B_C = input()
    B_C = B_C.split(' ')
    B = int(B_C[0])
    C = int(B_C[1])

    total = 0

    for a_i in A_i :
        # 총감독이 감독하고 남은 수
        others = a_i - B
        total += 1
        # 총감독이 모두 감독할 수 있는 경우
        if others <= 0 :
            continue
        # 부감독이 필요한 경우
        else :
            total += math.ceil(others/C)

    
    print(total)
            
