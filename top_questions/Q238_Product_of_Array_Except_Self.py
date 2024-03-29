class Solution:
    # Space: O(1)
    # Time: O(N)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length 

        # Left -> Right 
        result[0] = 1 
        for i in range(1, length): 
            result[i] = result[i - 1] * nums[i - 1]

        # Right -> Left
        right = 1
        for i in reversed(range(length)):
            result[i] *= right 
            right *= nums[i]

        return result 
