class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = collections.defaultdict(list)
           
        
        for i in range(len(strs)):
            newList = [0] * 26
            for j in strs[i]:
                c = ord(j) - ord('a')
                newList[c] += 1
            hmap[tuple(newList)].append(strs[i])
            
        return hmap.values()
            
            
        
        