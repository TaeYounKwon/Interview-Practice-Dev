def adder(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))

def solution(a, b):
    answer = 0
    if a==b:
        return a 
    else:
        if b>a:
            for i in range(a,b+1):
                answer+=i
        else:
            for i in range(b,a+1):
                answer+=i

    return answer
