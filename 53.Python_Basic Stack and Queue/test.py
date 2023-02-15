def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    before = -1
    for val in arr:
        if len(answer)==0:
            answer.append(val)
        elif answer[-1] != val:
            answer.append(val)
            
    return answer