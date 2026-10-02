def solution(n):
    answer = 0
    li = list(str(n)) 
# li라는 변수에 정수 n값을 문자열로 바꿔서 리스트형태로 추가
    for i in li:
        answer += int(i)
# li안에 문자열로 들어가있으니 누적합할때는 정수값으로 변경해줘야함
    return answer