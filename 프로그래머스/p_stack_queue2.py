def solution(priorities, location):
    doc_len = len(priorities)
    documents = [i for i in range(len(priorities))]
    answer = []
    while len(answer) < doc_len :
        first = priorities[0]
        priorities = priorities[1:]
        doc_first = documents[0]
        documents = documents[1:]
        if list(filter(lambda x : x>first, priorities)) :
            priorities.append(first)
            documents.append(doc_first)
        else :
            answer.append(doc_first)
    return answer.index(location)+1

print(solution([2, 1, 3, 2]	, 2))
print(solution([1, 1, 9, 1, 1, 1], 0))