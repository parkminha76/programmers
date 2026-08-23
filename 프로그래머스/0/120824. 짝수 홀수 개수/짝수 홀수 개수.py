def solution(num_list):
    even = 0 #짝수의 개수를 담을 변수 설정
    odd = 0 #홀수의 개수를 담을 변수 설정


    for i in num_list:
        if i%2==0: #짝수이면
            even+=1 #짝수 변수에 1씩 더하기
        else:
            odd+=1 #그 외, 홀수이면 훌수 변수에 1씩 더하기

    answer=[even, odd]

    return answer
    