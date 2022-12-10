# Find how many increasing numbers by 1 can create certain Number

# ex) '15'
# 1 + 2 + 3 + 4 + 5 = 15
# 4 + 5 + 6 = 15
# 7 + 8 = 15
# 15 = 15

# therefore, '15' has 4 method, result = 4

def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        tmpVal = i
        # print('Current: ',tmpVal)
        if tmpVal ==n:
            answer+=1
            # print('Final answer: ',answer)
            return answer
        for j in range(i+1,n):
            tmpVal+= j
            if tmpVal<n:
                pass
            elif tmpVal == n:
                 answer+=1
                #  print('Answer Count: ',answer)
                 break
            else:
                break              
        
    

# Sample Int
s1 = 15
s2 = 3

# Test Cases

if solution(s1)==4:
    print("Test 1 Passed")
else:
    print("Test 1 Failed")
    
if solution(s2)==2:
    print("Test 2 Passed")
else:
    print("Test 2 Failed")    
    
    
# Other's Answer - 등차수열!

# def expressions(num):
#     return len([i  for i in range(1,num+1,2) if num % i is 0])    
            