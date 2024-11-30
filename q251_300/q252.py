class Solution:
    # Time: O(N logN)
    # Space: O(1)
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sort by start time 
        intervals = sorted(intervals, key=lambda x: x[0])

        for i in range(len(intervals) - 1): 
            if intervals[i][1] > intervals[i+1][0]: 
                return False 

        return True 
        
