class Solution:
    # Space: O(1)
    # Time: O(N)
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]
        for num in nums: 
            curSum = max(curSum, 0) + num
            maxSum = max(maxSum, curSum)
        return maxSum
        
