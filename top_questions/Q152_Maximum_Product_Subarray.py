class Solution:
    # Space: O(1)
    # Time: O(N)
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        left = 1 
        right = 1
        length = len(nums)
        for i in range(length):
            left *= nums[i]
            right *= nums[length - 1 - i]
            result = max(result, max(left, right))
            if (left == 0):
                left = 1
            if (right == 0):
                right = 1
        return result 
        
