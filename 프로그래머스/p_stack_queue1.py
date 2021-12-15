import math

def solution(progresses, speeds):
    days = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    answer = {}
    for day in days :
        if not list(answer.keys()) :
            answer[day] = 1
        elif list(answer.keys()) and max(list(answer.keys())) >= day :
            answer[max(list(answer.keys()))] += 1
        elif list(answer.keys()) and max(list(answer.keys())) < day :
            answer[day] = 1
            
    return [answer[a] for a in answer.keys()]

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))