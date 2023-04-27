def solution(s):
    # 수가 홀수일때 바로 return
    if len(s)%2==1:
        return 0
    tmp = [] # 변수를 담을 리스트
    for i in s:
        if len(tmp)==0: # 리스트가 비어있으면 추가
            tmp.append(i)

        elif i==tmp[-1]: # 리스트가 안비워져 있고, 전번째 문자와 같으면, 전번째 문자 삭제(pop)
            tmp.pop()
        else:
            tmp.append(i) # 리스트가 비워져 있지 않고, 전번째 문자와 다르면 문자 추가

    # for loop후 글자가 짝지어져 있으면 len(tmp)==0
    if len(tmp)==0:
        return 1
    else:
        return 0