## 27. Remove Element


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        ## Sol. 1
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k = k + 1
        return k

        ## Sol. 2   
        # i = 0
        # while i < len(nums):
        #     if nums[i] == val:
        #         nums.pop(i)
        #         continue
        #     i += 1
  



        return len(nums)