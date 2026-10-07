def solution(arr):
    answer = []
    
    for i in arr:
        if answer == []:
            answer.append(i) # 첫 번째 조건문
        
        else:
            if i != answer[-1]: # 두 번째 조건문
                answer.append(i)
    return answer