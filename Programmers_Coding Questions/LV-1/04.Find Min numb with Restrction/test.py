def solution(n):
    answer = 0
    min_numb = 1000000
    for i in range(1,n):
        if n%i==1:
            if min_numb > i:
                min_numb = i
    answer = min_numb
    return answer

# 방법 2 
def solution2(n):
    return [x for x in range(1,n+1) if n%x==1][0]

