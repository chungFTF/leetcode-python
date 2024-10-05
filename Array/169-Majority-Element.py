# 169. Majority Element


class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        # Sol.3 Moore Voting Algorithm O(n)
        count = 0
        candidate = 0
         
        for num in nums:

            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

        # Sol. 1
        # my_dict = {}
        # for ele in nums:
        #     if ele not in my_dict:
        #         my_dict[ele] = 1
        #     else:
        #         my_dict[ele] += 1
            
        #     if my_dict[ele] > (len(nums)) // 2:
        #         return ele

        # Sol. 2
        # n = len(nums)
        # m = defaultdict(int)
        
        # for num in nums:
        #     m[num] += 1
        
        #     if m[num] > (n//2):
        #         return num
        
        # return 0


