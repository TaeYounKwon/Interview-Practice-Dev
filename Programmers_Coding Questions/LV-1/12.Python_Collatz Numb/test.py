def solution(num):
    cnt = 0
    if num == 1:
        return 0
    
    while num!=1:
        if num % 2 == 1:
            num = num*3 +1 
        else:
            num = num/2 
        cnt +=1
        if num == 1:
            break
        elif cnt >500:
            return -1
    
    return cnt

# 방법 2
def collatz(num):
    for i in range(500):
        num=num/2 if num%2==0 else num*3+1
        if num==1:
            return i+1
    return -1