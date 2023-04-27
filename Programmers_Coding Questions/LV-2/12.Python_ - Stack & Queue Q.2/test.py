def solution(p, s):
    answer = []

    for i in range(len(p)):
        p[i] = 100 - p[i]
        if p[i]%s[i] == 0:
            p[i]= p[i]//s[i]
        else:
            p[i] = p[i]//s[i]+1
    cnt = 0
    before = -1
    for i in range(len(p)):
        if i == 0:
            before = p[i]
            cnt = 1
        elif p[i]> before:
            answer.append(cnt)
            cnt = 1
            before = p[i]
        elif p[i]<=before:
            cnt+=1 

        if i == len(p)-1:
            if p[i]<=before:
                answer.append(cnt)


    return answer

def solution2(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]