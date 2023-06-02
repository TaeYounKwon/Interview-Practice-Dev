# 얀에서는 매년 달리기 경주가 열립니다. 
# 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다. 
# 예를 들어 1등부터 3등까지 "mumu", "soe", "poe" 선수들이 순서대로 달리고 있을 때, 
# 해설진이 "soe"선수를 불렀다면 2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다. 
# 즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.

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

