import re

test = "a+b-(b/c-((a+b)/c))"
# test1 = 'a+b*c+d'
# test='A*(B+C)'

def toPostfix(notation) :
    print(notation)
    stack = []
    for n in notation :
        if stack and (stack[-1] == '*' or stack[-1] =='/') :
            symbol = stack.pop()
            char = stack.pop()
            push = char + n + symbol
            stack.append(push)
        else :
            stack.append(n)
    
    semi_result = ''
    while stack :
        p = stack[0]
        stack = stack[1:]
        if p == '+' or p == '-' :
            semi_result += p
        else :
            if semi_result :
                semi_result = semi_result[:-1] + p + semi_result[-1]
            else :
                semi_result += p
    
    return semi_result

def entirePostfix(notation) :
    stack = []

    count_left = 0
    count_right = 0

    for n in notation :
        stack.append(n)
        if n == '(' :
            count_left +=1
        elif n == ')' :
            count_right += 1
        
        save_l = count_left
        # 괄호가 한 세트 완성되었을 때
        if count_left > 0 and count_right > 0 :
            semi_result = ''
            while count_left == save_l :
                p = stack.pop()
                if p == ')' :
                    count_right -= 1
                elif p == '(' :
                    count_left -= 1
                else :
                    semi_result = p + semi_result
            
            stack.append(toPostfix(semi_result))
        print(stack)
    
    # stack 변환
    save = []
    symbols = ['+', '-', '*', '/']
    for s in range(len(stack)) :
        if stack[s] not in symbols :
            save.append(stack[s])
            stack[s] = str(len(save)-1)
    
    result = toPostfix(''.join(stack))
    for i in range(len(save)) :
        result = result.replace(str(i), save[i])

        
    
    return result

print(toPostfix('A+B+C'))
# print(entirePostfix(test))  




                



    

# items = re.findall('\(([^)]+)', test1)
