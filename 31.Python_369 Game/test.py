def solution(order):
    answer = 0
    tmp = str(order)
    answer = tmp.count('3')+tmp.count('6')+tmp.count('9')
    
    return answer

if solution(29423) == 2:
    print('Pass')
else:
    print('Failed')