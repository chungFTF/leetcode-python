# 53-maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        ans = nums[0]
        sums = 0

        for ele in nums:
            if sums > 0:
                sums += ele
            else:
                sums = ele
            ans = max(sums, ans)

        return ans        

