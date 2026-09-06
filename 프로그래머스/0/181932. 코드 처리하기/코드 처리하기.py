def solution(code):
    answer = ''
    mode = 0

    for idx, i in enumerate(code):
        # enumerate 사용 시, 인덱스의 위치와 인덱스 값을 같이 가져올 수 있음.
        # 여기서 idx가 인덱스 위치이고 i가 인덱스 값
        if i != "1":
            if mode == 0 and idx % 2 == 0:
                answer += i
            elif mode == 1 and idx % 2 == 1:
                answer += i
        else:
            mode = 1 - mode

    
    if answer == '':          # answer가 비어있으면
        return "EMPTY"        # "EMPTY" 반환
    return answer              # 아니면 원래대로 반환