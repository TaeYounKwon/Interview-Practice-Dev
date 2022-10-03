import math
import os
import re
import random
import re
import sys
import math

def checkPerfectSquare(p):
    if(p>=0):
        tmp = int(math.sqrt(p))
        return ((tmp*tmp)==p)
    
    return False

def canReach(c, x1, y1, x2, y2):
    # Write your code here
    if c<0:
        return "No"
    elif checkPerfectSquare(x1+y1):
        return "No"
    elif checkPerfectSquare(x2+y2):
        return "No"
    else:
        #find max coordinate to create the 2D matrix
        maxC = max(x1,y1,x2,y2)
        #Create matrix with maxC+1 size
        tmpList = [[0 for i in range(maxC+1)] for j in range(maxC+1)]
        #Set the starting coordinate
        tmpList[x1][y1]=1
        
        for i in range(x1,maxC+1):
            for j in range(y1,maxC+1):
                #if starting point, pass
                if (i==x1 and j==y1):
                    continue
                #if perfectsquare, pass
                elif checkPerfectSquare(i+j):
                    continue
                #check if it is reachable or not
                elif (i-c)>-1 and (j-c)>-1 and tmpList[i-c][j-c]==1:
                    tmpList[i][j]=1
                elif tmpList[i-j][j]==1 or tmpList[i][j-1]==1:
                    tmpList[i][j]=1    
    
        if tmpList[x2][y2]==1:
            return "Yes"
        
        return "No"
    
        
    

c = 2

x1 = 1

y1 = 3

x2 = 25

y2 = 33

result = canReach(c, x1, y1, x2, y2)

print(result)
