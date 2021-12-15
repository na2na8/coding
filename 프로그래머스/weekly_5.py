import itertools
import re

def solution(word):
    case = list(filter(lambda x : re.compile('^\w+\s*$').match(x), [''.join(w) for w in list(itertools.product(([' ', 'A', 'E', 'I', 'O', 'U']), repeat=5))]))
    case.sort()
    return case.index(word.ljust(5))+1


w1 = "AAAAE"	#6
print(solution(w1))
w2 = "AAAE"	#10
print(solution(w2))
w3 = "I"	#1563
print(solution(w3))
w4 = "EIO"	#1189
print(solution(w4))