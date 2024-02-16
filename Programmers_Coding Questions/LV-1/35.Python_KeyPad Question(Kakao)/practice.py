def solution(numb, hand):
    tmp = {1:'L', 4:'L', 7:'L', 3:'R', 6:'R', 9:'R'}
    mid = {2:[[2],[1,3,5],[4,6,8],[7,0,9],['*','#']],
           5:[[5],[2,4,6,8],[1,3,7,9,0],['*','#']],
           8:[[8],[5,7,9,0],[4,6,'*','#',2],[1,3]],
           0:[[0],['*','#',8],[7,9,5],[2,4,6],[1,3]]  
          }
    answer = ''
    left = '*'
    right = '#'
    for n in numb:
        if n in tmp:
            answer+=tmp[n]
            if tmp[n]=='L':
                left = n
            else:
                right = n
        else:
            l_dis = 10
            r_dis = 10
            lst = mid[n]
            for i in range(len(lst)):
                if left in lst[i]:
                    l_dis = i 
                if right in lst[i]:
                    r_dis = i
            
            if l_dis<r_dis:
                left = n 
                answer+='L'
            elif r_dis<l_dis:
                right = n 
                answer+='R'
            else:
                if hand == 'left':
                    left = n 
                    answer+='L'
                else:
                    right = n 
                    answer+='R'
                     
    
    return answer

numb = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = 'right'
answer = solution(numb,hand)
print(answer)