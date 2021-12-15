import time

def solution(citations) :
    n = len(citations)
    h = 5000
    get_max = []
    while True :
        time.sleep(0.1)
        over_h = [c for c in citations if c>=h]
        under_h = [c for c in citations if c<=h]
        l_over = len(over_h)
        l_under = len(under_h)
        print(h, get_max, l_over, l_under)
        if l_over >= h and l_under <= h :
            get_max.append(h)
            h = h+1
        elif l_over < h and len(get_max) == 0 :
            h = h+int(min((n-h), h)/2)
        elif l_under > h and len(get_max) == 0:
            h = h-int(min((n-h), h)/2)
        else :
            
            max_ = max(get_max)
            return max_

test = [53, 26, 20, 13, 10, 4, 2]

print(solution(test))