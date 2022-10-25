
def solution(A,B):
    # Sort the two list ( B with reverse=True) to create the minimum sum of two multiplied numbers
    A.sort()
    B.sort(reverse=True)
    
    # Put sorted lists into tmp1 and tmp2
    tmp1 = A
    tmp2 = B
    
    # Calculate minimum sum of multiplied numbers
    answer = 0
    for i in range(len(tmp1)):
        answer += tmp1[i]*tmp2[i]

    return answer


# sample list
s1 = [1,4,2]
s2 = [5,4,4]
s3 = [1,2]
s4 = [3,4]

# Test cases
if solution(s1,s2)==29:
    print("Test 1 Passed")
else:
    print("Test 1 Failed") 
       
if solution(s3,s4)==10:
    print("Test 2 Passed")    
else:
    print("Test 2 Failed")    