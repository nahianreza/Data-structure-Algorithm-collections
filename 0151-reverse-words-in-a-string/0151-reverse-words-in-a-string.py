class Solution:
    def reverseWords(self, s: str) -> str:
        # Go over the intitial string and append the words to a list
        # Go over the list and reverse
        # Add the items from the reversed list to a new string
        
        resList = []
        word = ""
        s = s.lstrip()
        s = s.rstrip()
        
        if len(s) == 1:
            return s
        
        for c in s:
            if c == ' ':
                if word:
                    resList.append(word)
                    word = ""
                continue
            word += c
        
        resList.append(word)
        
        left, right = 0, len(resList) - 1
        
        while right > left:
            temp = resList[left]
            resList[left] = resList[right]
            resList[right] = temp
            
            left += 1
            right -= 1
            
        resString = ""
        
        for i in range(len(resList)):
            resString += resList[i]
            
            if i!= len(resList) - 1:
                resString += " "
        
        return resString
            
                
                