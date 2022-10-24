import sys

#Solution function
def solution(s):
    
    # Divide the String with " " value
    tmp = s.split(" ")
    
    # Variable to find the min and max value from the "tmp" list
    minVal = sys.maxsize
    maxVal = -(sys.maxsize + 1)
    currentVal = 0
    
    for i in range(len(tmp)):
        # if the list value is negative number
        if "-"in tmp[i]:
            # remove - sign, then change the value from str to int and multiply by -1
            tmpVal = tmp[i].replace('-','')
            currentVal = -1 * int(tmpVal)
            # check min and max value
            if currentVal > maxVal:
                maxVal = currentVal
            if currentVal < minVal:
                minVal = currentVal
           
        else:
            # check min and max value
            currentVal = int(tmp[i])
            if currentVal > maxVal:
                maxVal = currentVal
            if currentVal < minVal:
                minVal = currentVal
    
    # add up the minVal and maxVal to str answer and check       
    answer = str(minVal)+' '+str(maxVal)                
    print(answer)
    #return(answer)      



a="-1 -2 -3 -4"
solution(a) 

b='1 3 4 -7'
solution(b)

c='-800 7500 600 300'
solution(c)