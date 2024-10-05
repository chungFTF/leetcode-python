# 189. Rotate Array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Sol.1 (Runtime beats 78%, Mem beats 33%)
        # 先抽後面 k 個 -> 把前面剩下的往後 k 步（記得存原始值）-> 把原先後面的原始直補回前面

        # simplified_k = k % len(nums)
        # temp_data = nums[num_len - simplified_k: num_len]
        # for i in range(num_len - simplified_k - 1, -1, -1):
        #     nums[i+simplified_k] = nums[i]

        # for j in range(len(temp_data)):
        #     nums[j] = temp_data[j]
        # print(nums)


        # Sol.2 (Runtime beats 78%, Mem beats 71%)
        temp_data = nums.copy()
        for position in range(len(nums)):
            new_position = (k + position) % len(nums)
            nums[new_position] = temp_data[position]
        # print(nums)

