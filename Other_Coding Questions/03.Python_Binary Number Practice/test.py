# Step 1. Remove all '0' value from the string 'x'
# Step 2. c = length of remain 'x'
# Step 3. Change the 'c' to binary number
# Step 4. Repeate the Step 1 to 3 until 'x' becomes 1
# Step 5. Return [how many step required, removed number of '0']



def solution(s):
    #Variables to check
    copiedList = s
    countZero = 0
    countOne = 0
    countSteps = 0
    
    # If s = ['1'], return immediately
    if s.count('1')==1 and s.count('0')==0:
        return ([0,0])
    else:
        while(True):
            if (countOne == 1):
                break
            
            countSteps += 1
            
            # Step 1.
            countZero += copiedList.count('0')
            tmp= copiedList.replace('0','')
           
            # Step 2.
            countOne = tmp.count('1')
            
            # Step 3.
            toBinary = format(int(countOne),'b')
           
           # Repeat the step
            copiedList = toBinary

    answer = [countSteps,countZero]
    return answer


# Sample List
s1="110010101001"	
s2="01110"
s3="1111111"
s4='10'
# Test Cases 1
if solution(s1)==[3,8]:
    print("Test 1 Passed")
else:
    print("Test 1 Failed")    
    
# # Test Cases 2
if solution(s2)==[3,3]:
    print("Test 2 Passed")
else:
    print("Test 2 Failed")    
    
# # Test Cases 3
if solution(s3)==[4,1]:
    print("Test 3 Passed")
else:
    print("Test 3 Failed")         

# Test Cases 4
if solution(s4)==[1,1]:
    print("Test 4 Passed")
else:
    print("Test 4 Failed")      