from typing import List

class twoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        answer = [0, 0]
        
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    
                
nums = [2,7,11,15]
test = twoSum()
print(test.twoSum(nums, 9))
