# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(p, c):
    answer = []
    rank = dict()
    name = dict()
    for i in range(len(p)):
        name[p[i]] = i
        rank[i] = p[i]
        
    for i in c:
        before = name[i]
        tmp_name = rank[before-1]
        name[i] -= 1
        name[tmp_name] +=1
        rank[before] = tmp_name
        rank[before-1] = i
    
    
    for keys, vals in rank.items():
        answer.append(vals)
    return answer