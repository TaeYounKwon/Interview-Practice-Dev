def solution(seoul):
  
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

# 방법 2
def solution(seoul):

    index = seoul.index('Kim')
    answer = '김서방은 '+str(index) +'에 있다'
    return answer