from collections import deque

def solution(n, edge):
    answer = 0
    distance = [0]*(n+1)
    edge.sort()
    queue = deque()
    graph = [[] for i in range(n+1)] # [[], [], [], [], [], [], []]
    
    # 양 방향성임으로 2번 더함, 더한뒤 그래프는  [[], [2, 3], [1, 4, 3, 5], [1, 2, 6, 4], [2, 3], [2], [3]]
    for e in edge: 
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    queue.append(1)
    distance[1] = 1
    
    while queue:
        current = queue.popleft()
        
        for g in graph[current]:
            if distance[g] ==0:
                queue.append(g)
                distance[g] = distance[current] +1
                
        
    max_distance = max(distance)
    for i in distance:
        if i == max_distance:
            answer+= 1
    
    return answer