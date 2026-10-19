def solution(a, b):
    answer = 0
    
    for i in range(a,b+1):
        answer += i
    
    for i in range(b,a+1):
        answer += i
        
    if a == b:
        answer = a
    return answer