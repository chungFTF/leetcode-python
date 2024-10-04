# 209. Minimum Size Subarray Sum



class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        min_len = float('inf')
        sums = 0
        
        while right < len(nums):
            sums += nums[right] 

            while sums >= target:
                min_len = min(min_len, right - left + 1)
                sums -= nums[left]
                left += 1

            right += 1

        return min_len if min_len != float('inf') else 0

