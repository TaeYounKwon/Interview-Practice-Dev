def solution(coin, money):
    answer = {}
    coin.sort(reverse = True)

    for m in coin:
        tmp = 0
        if money>=m:
            tmp = money//m
            answer[m] = tmp
            money -= tmp*m 
    
    print(answer)
    # for i in range(len(coin)):
    
        
        
    return answer 

coin = [50,10, 100, 500,1000,5000 ]
money = 38270

result = solution(coin, money)