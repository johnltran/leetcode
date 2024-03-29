class Solution:
    # Space: O(N) 
    # Time: O(N)
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() 
        for num in nums: 
            if num in seen: 
                return True 
            seen.add(num)
        return False 
