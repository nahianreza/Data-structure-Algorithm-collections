class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        res = 0
        visited = set(beginWord)
        wordList.append(beginWord)

        hmap = collections.defaultdict(list)  

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                hmap[pattern].append(word)

        queue = collections.deque()

        queue.append(beginWord)

        while queue:
            res += 1
            for i in range(len(queue)):
                popped = queue.popleft()
                if popped == endWord:
                    return res
                for i in range(len(popped)):
                    pattern = popped[:i] + "*" + popped[i + 1:]
                    neighbors = hmap[pattern]
                    for n in neighbors:
                        if n in visited:
                            continue
                        visited.add(n)
                        queue.append(n)
        
        return 0




    

    
        