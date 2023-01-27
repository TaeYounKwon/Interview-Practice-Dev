def solution(n):
    ls = list(str(n))
    ls.sort(reverse=True)
    return int(''.join(ls))

def solution(n):
    n = str(n)
    tmp = list(n.strip(''))
    tmp.sort(reverse=True)
    answer = ''
    for i in tmp:
        answer+= i
    answer = int(answer)
    return answer