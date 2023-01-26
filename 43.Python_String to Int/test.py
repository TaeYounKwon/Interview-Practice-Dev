def solution(s):
    answer = 0
    
    if s[:1].isdigit():
        return int(s)
    else:
        if s[:1]== '-':
            tmp = int(s[1:]) * -1
        else:
            tmp = int(s[1:])
        return tmp    

# 방법 2
def strToInt(str): 
    result = 0
    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)
    return result