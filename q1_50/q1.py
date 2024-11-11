class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # map: num -> index 
	# Time: O(N) 
	# Space: O(N) 
        m_map = {} 
        for idx, num in enumerate(nums): 
            complement = target - num 
            if complement in m_map: 
                return [m_map[complement], idx]
            
            m_map[num] = idx 

        return []
