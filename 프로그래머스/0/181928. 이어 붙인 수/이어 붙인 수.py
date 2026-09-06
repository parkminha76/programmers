def solution(num_list):
    answer = 0
    odd_list = ''
    even_list = ''

    for i in num_list:          
        if i % 2 == 1:
            odd_list += str(i)   # 정수를 문자열로 바꿔서 이어 붙임
        else:
            even_list += str(i)

    return int(odd_list) + int(even_list)   # 각각 문자열을 다시 숫자로 바꿔서 합산