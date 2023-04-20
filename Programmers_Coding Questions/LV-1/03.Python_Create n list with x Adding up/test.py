def solution(x, n):
    answer = []
    for i in range(1,n+1):
        tmp = x*i
        answer.append(tmp)
    return answer

# 방법 2
def number_generator(x, n):
    # 함수를 완성하세요
    return [i * x + x for i in range(n)]