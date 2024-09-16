class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxString = ""
        resLen = 0
        
        for i in range(len(s)):
            left, right = i , i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    maxString = s[left:right + 1]
                    resLen = right - left + 1
                left -= 1
                right += 1
              
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    maxString = s[left:right + 1]
                    resLen = right - left + 1
                left -= 1
                right += 1

            
        
        return maxString
                
        