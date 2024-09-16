class Solution:
    def reverseWords(self, s: List[str]) -> None:
        
        if len(s) == 1:
            return s
        

        left, right = 0, len(s) - 1
        while right > left:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        left = right = 0

        while right < len(s):
            if s[right] == " " or right == len(s) - 1:
                l = left
                if right == len(s) - 1:
                    r = right
                else:
                    r = right - 1

                while r > l:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
                left = right = right + 1
            
            right += 1

        

        
        

        
        return s
