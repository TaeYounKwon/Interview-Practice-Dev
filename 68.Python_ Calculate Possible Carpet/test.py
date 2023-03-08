def solution(brown, yellow):
    answer = []
    tmp = []
  
    for i in range(1,yellow+1):
        cal_val = yellow % i
        if cal_val == 0:
            add_val = yellow // i
            tmp.append([i,add_val])

    is_valid = False
    for i in range(len(tmp)):
        val1 = tmp[i][0]
        val2 = tmp[i][1]
        val_cal = (val1+2) * (val2+2) - yellow
        if val_cal == brown:
            if val2>val1:
                answer.append(val2+2)
                answer.append(val1+2)
            else:
                answer.append(val1+2)
                answer.append(val2+2)
                
            return answer
    
    if is_valid == False:
        return False

def solution2(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]