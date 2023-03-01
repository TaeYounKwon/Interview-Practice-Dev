def solution(s):
    cnt_zero = 0
    cnt_step = 0
    tmp = 0
    while True:
        cnt_step += 1
        cnt_zero += s.count('0')
        s = s.replace('0','')
        tmp = len(s)
        
        if tmp == 1:
            return [cnt_step,cnt_zero]
            break
        else:
            tmp = bin(tmp)
            s = tmp[2:]
            
def solution2(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]