# 485. Max Consecutive Ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        # Sol. 2
        max_k = local_k = 0
        for i in nums:
            if i == 1:
                local_k += 1
                max_k = max(local_k, max_k)
            else:
                local_k = 0
        return max_k



        # Sol. 1
        # i = 0
        # max_k = 0

        # while (i+1) <= len(nums):
        #     print(i)
        #     j = i + 1

        #     if nums[i] != 1:
        #         i += 1
        #         continue
        #     else:
        #         local_k = 1
        #         while j <= len(nums) - 1:
        #             if nums[j] == 1:
        #                 local_k += 1
        #                 j += 1
        #             else:
        #                 break
        #         max_k = max(local_k, max_k)
        #         i = j+1

        # return max_k
            

        