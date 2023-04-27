def solution(routes):
    answer = 1
    routes.sort(reverse=True)

    for i in range(len(routes)):
         routes[i].sort(reverse=True)   
    print(routes)
    n_min = 0
    n_max = 0
    for i in range(len(routes)):
        n_max=routes[i][0]
        if i == 0:
            n_min = routes[i][1]
        elif n_max<n_min:
            answer+=1
            n_min = routes[i][1]

    return answer
