def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    j = len(people) -1
    for i in range(len(people)):
        if i==j:
            answer+=1
            break
        elif i>j:
            break
        
        if people[i] + people[j]>limit:
            pass
        else:
            j-=1
        answer +=1
        
    return answer