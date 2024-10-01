# 977. Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        left, right = 0, len(nums) - 1
        k = len(nums) - 1
        new_nums = [0] * len(nums)
        
        while(left <= right):
            if(nums[right]**2 > nums[left]**2):
                new_nums[k] = nums[right]**2
                right -= 1
            else:
                new_nums[k] = nums[left]**2
                left+= 1
            k -= 1
            
        return new_nums

