def solution(people, limit):
    answer = 0

    while(True):
        print(people)
        n_max = max(people)
        n_min = min(people)
        if n_max == n_min :
            if len(people)==1:
                people.remove(n_min)
                
                
            else:
                if n_min + n_max > limit:
                    people.remove(n_max)
                else:
                    people.remove(n_max)
                    people.remove(n_min)
        else:
            if n_max + n_min > limit:
                people.remove(n_max)
            else:
                people.remove(n_min)
                people.remove(n_max)
        answer+=1
        if len(people)==0:
            break
            
    return answer

if solution( [70,50,80,50],100) == 3:
    print('Solved!')
else:
    print('Wrong')