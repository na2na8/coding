import time

def h_index(citations, n, h, get_max) :
    over_h = [c for c in citations if c>=h]
    under_h = [c for c in citations if c<=h]
    l_over = len(over_h)
    l_under = len(under_h)
    if l_over >= h and l_under <= h :
        get_max.append(h)
        return h_index(citations, n, h+1, get_max)
    elif l_over < h and len(get_max) == 0 :
        return h_index(citations, n, h+int(min((n-h), h)/2), get_max)
    elif l_under > h and len(get_max) == 0:
        return h_index(citations, n, h-int(min((n-h), h)/2), get_max)
    else :
        max_ = max(get_max)
        return max_

def solution(citations) :
    n = len(citations)
    init_h = int(n/2)
    h = h_index(citations, n, init_h, [])
    return h

    



test = [53, 26, 20, 13, 10, 4, 2]

print(solution(test))