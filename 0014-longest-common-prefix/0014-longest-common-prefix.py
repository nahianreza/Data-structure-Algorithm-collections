
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        res = ""
        strs.sort(key = len)
        print(strs)

        for i, val in enumerate(strs[0]):
            for nextVal in strs[1:]:
                if nextVal[i] != val:
                    return res
            else:
                res += val

        return res

      




        
            



        