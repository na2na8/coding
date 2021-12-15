import hashlib
from pprint import pprint
def solution(participant, completion):
    hash_dic = {}
    h = hashlib.sha256()
    for c in completion :
        h.update(c.encode('utf-8'))
        hash_dic[h.hexdigest()] = c
    pprint(hash_dic)
    m = hashlib.sha256()
    for p in participant :
        try :
            m.update(p.encode('utf-8'))
            result = m.hexdigest()
            print(result, p)
            hash_dic[result]
        except KeyError :
            return p

print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))	#"leo"
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))	#"vinko"
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))	#"mislav"