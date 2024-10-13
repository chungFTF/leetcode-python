class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    
        # Sol. 1 O(log(m+n))
        # 確保 nums1 是較小的數組
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        n1, n2 = len(nums1), len(nums2)
        left, right = 0, n1
        
        # 使用二分搜索法找到正確的分割位置
        while left <= right:
            # 計算 nums1 和 nums2 的分割位置
            partitionX = (left + right) // 2
            partitionY = (n1 + n2 + 1) // 2 - partitionX
            
            # 計算左右子數組的邊界值
            maxLeftX = nums1[partitionX - 1] if partitionX != 0 else float('-inf')
            minRightX = nums1[partitionX] if partitionX != n1 else float('inf')
            
            maxLeftY = nums2[partitionY - 1] if partitionY != 0 else float('-inf')
            minRightY = nums2[partitionY] if partitionY != n2 else float('inf')
            
            # 如果分割正確,返回中位數
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (n1 + n2) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            
            # 否則,根據大小關係更新 left 或 right 指針
            elif maxLeftX > minRightY:
                right = partitionX - 1
            else:
                left = partitionX + 1
        
        # 如果未找到正確的分割位置,拋出異常
        raise ValueError
        
        
# Sol. 2 Two-Pointer Method O(m+n)
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         total_len = len(nums1) + len(nums2)
#         idx_1 = idx_2 = count = 0
#         total_nums = []

#         while count <= (total_len//2):
#             if idx_1 >= len(nums1):
#                 total_nums += nums2[idx_2:]
#                 break
            
#             if idx_2 >= len(nums2):
#                 total_nums += nums1[idx_1:]
#                 break

#             if nums1[idx_1] < nums2[idx_2]:
#                 total_nums.append(nums1[idx_1])
#                 idx_1 += 1
#             else:
#                 total_nums.append(nums2[idx_2])
#                 idx_2 += 1

#             count += 1
        
#         if (total_len % 2) == 0:
#             return (total_nums[(total_len//2)-1] + total_nums[total_len//2]) / 2
#         else:
#             return total_nums[total_len//2]
            
            