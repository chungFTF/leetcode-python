# 26 remove-duplicates-from-sorted-array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Sol. 1 Beats 92%

        cur = 0
        move = 1
        k = 1
        while(cur < len(nums) and move < len(nums)):

            if(nums[cur] == nums[move]):
                move += 1
            else:
                nums[cur + 1] = nums[move]
                cur += 1
                k += 1
        # print(nums)
        return k

  
        # # Sol. 2
        # j = 1
        # for i in range(1,len(nums)):
        #     if nums[i] != nums[i-1]:
        #         nums[j] = nums[i]
        #         j += 1
        # return j

        