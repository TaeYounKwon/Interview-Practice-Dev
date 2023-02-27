def solution(s):
    answer = True
    
    if s[0] == ')':
        return False
    cnt = 0
    for tmp in s:
        if tmp == '(':
            cnt+=1
        else:
            cnt-=1
        if cnt <0:
            return False
        
    if cnt !=0:
        return False

    return True

def is_pair(s):
    pair = 0
    for x in s:
        if pair < 0: break
        pair = pair + 1 if x == "(" else pair - 1 if x == ")" else pair
    return pair == 0