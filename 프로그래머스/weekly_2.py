def solution(scores):
    answer = ''
    for student in range(len(scores)) :
        stud_scores = list(list(zip(*scores))[student])
        if (stud_scores[student] == max(stud_scores) or stud_scores[student] == min(stud_scores)) and stud_scores.count(stud_scores[student])==1 :
            del stud_scores[student]
        sum_scores = sum(stud_scores)/len(stud_scores)
        if sum_scores >= 90 :
            answer +='A'
        elif sum_scores >= 80 :
            answer += 'B'
        elif sum_scores >= 70 :
            answer += 'C'
        elif sum_scores >= 50 :
            answer += 'D'
        else :
            answer += 'F'
    return answer

test1 = [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]] #"FBABD"
print(solution(test1))
test2 = [[50, 90], [50, 87]] #"DA"
print(solution(test2))
test3 = [[70, 49, 90], [68, 50, 38], [73, 31, 100]] #"CFD"
print(solution(test3))