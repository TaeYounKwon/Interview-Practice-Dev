def solution(s):
    # Devide the str variable by space(" ")
    tmpVal = s.split(" ")
    
    # Change letters to lower case, then capitalize the first letter
    for i in range(len(tmpVal)):
        tmpVal[i] = tmpVal[i].lower()
        tmpVal[i] = tmpVal[i].capitalize()
        
    #add up the capitalized letters
    answer = ''
    for i in range(len(tmpVal)):
        if i<len(tmpVal)-1:
            answer=answer + tmpVal[i] + ' '   
        else:
             answer=answer + tmpVal[i]
    return answer


# Sample string
s1 = "3people unFollowed me"
s2 = "for the last week"
s3 = "mY nAMe iS hElLo wORLd"

# Test Cases
if solution(s1)=="3people Unfollowed Me":
    print("Test 1 Passed")
else:
    print("Test 1 Failed")    
    
if solution(s2)=="For The Last Week":
    print("Test 2 Passed")
else:
    print("Test 2 Failed")     
    
if solution(s3)=="My Name Is Hello World":
    print("Test 3 Passed")
else:
    print("Test 3 Failed")         