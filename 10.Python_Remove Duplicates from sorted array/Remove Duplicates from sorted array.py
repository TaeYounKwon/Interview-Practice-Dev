#Remove Duplicates from sorted array
class Solution(object):
    def removeDuplicates(self, nums):
        numb= len(nums)
        standVal = nums[0]
        position = 0
        lastVal = nums[numb-1]
        passTest = False
        for i in range (len(nums)-1):    
            nextVal = nums[i+1]
            if standVal == nextVal:
                pass
            elif standVal != nextVal:
                position +=1
                nums[position] = nextVal
                standVal = nextVal
                if standVal == lastVal:
                    passTest = True
                    
        popVal = numb - position -1   
        
        for j in range(popVal):
            newRange = len(nums)-1
            nums.pop(newRange)
            
            
    