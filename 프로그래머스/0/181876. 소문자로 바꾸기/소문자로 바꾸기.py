def solution(myString):
    answer = ''
    for i in myString:
        if i == i.upper():
            answer += i.lower()
        else:
            answer += i
    return answer