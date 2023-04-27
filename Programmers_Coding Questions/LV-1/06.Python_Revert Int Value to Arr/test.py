def solution(n):
    print(reversed(str(n)))
    
    return list(map(int, reversed(str(n))))

# 방법 2
def solution2(n):
    answer = []
    tmp = str(n)
    tmp = tmp[::-1]
    for i in tmp:
        answer.append(int(i))
    return answer