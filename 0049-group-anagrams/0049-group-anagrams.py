class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list)

        

        for i in strs:
            charList = [0] * 26
            for j in i:
                diff = ord(j) - ord('a')
                charList[diff] += 1
            hmap[tuple(charList)].append(i)
        
        return [x[1] for x in hmap.items()]

        
        
        