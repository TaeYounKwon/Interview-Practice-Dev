class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        loopOut = False
        tmp = []
        profitList = []
        
        for i in range(len(prices)):
            tmp.append([])
            profitList.append([])
            for j in range(len(prices)):
                tmp[i].append(0)
                profitList[i].append(0)
        
        maxProfit = 0 
       
        for i in range (len(prices)-1):
            tmp.append([])    
            for j in range (i+1,len(prices)):
                
                if prices[i]>=prices[j]:
                    tmp[i].append(0)
                    pass
                else:
                    priceDiff = 0
                    priceDiff = prices[j]-prices[i]
                    if priceDiff > maxProfit:
                        maxProfit =priceDiff
                        tmp[i][j]=maxProfit
                        maxProfit = 0 
       
        for i in range(len(tmp)):        
            for j in range(len(tmp[i])):
                if tmp[i][j] != 0:
                    profitList[j][i]=tmp[i][j]
        
        for i in range(len(profitList)):
            for j in range(len(profitList[i])):
                print(profitList[i][j],end=" ")
            print(' ')    
                    
                    
                    
        maxProfit = 0
        currentProfit = 0
        position = -1
        currentPosition = -1
        newPosition = 0
        dayGap = -1
        newDay = 0
        rival = False
        for i in range(len(profitList)):
            nextProfit = 0    
            
            for j in range(len(profitList[i])):
                if profitList[i][j]==0:
                    pass
                
                if profitList[i][j]>maxProfit:
                    
                    if position == j:
                        currentProfit = profitList[i][j]
                        print("currentProfit: ", currentProfit)
                        currentPosition = i
                        rival = True
                        
                    else: 
                        maxProfit = profitList[i][j]
                        dayGap = i
                        position = j
                       
                    
                    
                else:
                    if profitList[i][j]==0:
                        pass
                    elif j == position:
                        pass
                    elif j > position +1:
                            if i > dayGap +1:
                                if profitList[i][j]>nextProfit:
                                    nextProfit = profitList[i][j]
                                    print("nextProfit: ", nextProfit)
                                    newPosition = j
                                    newDay = i
                    else:
                        pass
            if rival == True:        
                if currentProfit>maxProfit+nextProfit:
                    maxProfit = currentProfit
                    newPosition = 0
                    dayGap = 0
                    rival == False
                else:
                    maxProfit += nextProfit
                    position = newPosition
                    dayGap = newDay
                    rival == False
                    
            print(i, ' maxProfit: ',maxProfit)    
        return maxProfit    
        