class Solution:
    def longestPalindrome(self, s: str) -> str:
        #babad

        maxString = ""
        maxLen = 0

        for i in range(len(s)):
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxString = s[l: r + 1]
                    maxLen = r - l + 1
                l -= 1
                r += 1
        

        
            l,r = i,i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxString = s[l: r + 1]
                    maxLen = r - l + 1
                l -= 1
                r += 1

        return maxString
        
            
        
        

        


        
                
        