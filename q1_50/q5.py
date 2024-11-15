class Solution:
    # Time: O(N^2)
    # Space: O(1)
    
    def expand(self, s: str, left: int, right: str) -> int: 
        while (left >= 0 and right < len(s) and s[left] == s[right]): 
            left -= 1 
            right += 1 

        return right - left - 1 


    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) < 2: 
            return s 

        start = 0
        end = 0 
        for i in range(len(s)):
            odd_len = self.expand(s, i, i)
            even_len = self.expand(s, i, i + 1)

            cur_len = max(odd_len, even_len) 
            if cur_len > (end - start): 
                start = i - (cur_len - 1) // 2 
                end = i + cur_len // 2 

        return s[start : end+1]
        
