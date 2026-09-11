def solution(n, t):
    answer = 0
    
    for i in range(t+1):
        if i == 0: # 그냥 제일 처음 0시간?
            answer = n          # 시작할 때는 원래 마릿수
        else:
            answer = answer * 2  # 한 시간 지날 때마다 2배씩 증가
            
    return answer