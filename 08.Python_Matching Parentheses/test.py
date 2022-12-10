def solution(s):
    # Divide the List by each elements
    tmp = list(s)
    count = 0
    # If list starts with ), return False
    if tmp[0]==')':
        return False
    else:
        for i in range(len(tmp)):
            #If ')' comes out before '(', then return False
            if count<0:
                return False
            if tmp[i]=='(':
                count+=1
            elif tmp[i]==')':
                count-=1    
        # Check if it's matching Parentheses        
        if count != 0:
            return False
        else:
            return True
    

# Sample String
s1 = "()()"
s2 = "(())()"	
s3 = ")()("
s4 = "(()("	

# Test Cases
if solution(s1)==True:
    print("Test 1 Passed")
    
if solution(s2)==True:
    print("Test 2 Passed")    

if solution(s3)!=True:
    print("Test 3 Passed")
    
if solution(s4)!=True:
    print("Test 4 Passed")        