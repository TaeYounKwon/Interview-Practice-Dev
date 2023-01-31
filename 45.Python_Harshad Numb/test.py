def solution(x):
    tmp = str(x)
    val = 0
    for i in tmp:
        val += int(i)
    if x % val ==0:
        return True
    else:
        return False
    
# 방법 2
def Harshad(n):
    return n%sum(int(x) for x in str(n)) == 0