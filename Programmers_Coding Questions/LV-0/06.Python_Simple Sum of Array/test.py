def solution(arr):
    return sum(arr)/len(arr)

def solution2(arr):
    answer = 0
    cnt = 0
    for i in arr:
        answer += i 
        cnt += 1
    answer = answer/cnt
    return answer