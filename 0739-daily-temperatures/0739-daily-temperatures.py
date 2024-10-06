# Initilize a list with len(temp) 0's
# go over the input list and append them on a stack
# if i greater than last value of stack, then pop last value, put the diff in the index and then append the cur val
# else just append
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sizeTemp = len(temperatures)
        res = [0] * sizeTemp
        stack = []
        for i, val in enumerate(temperatures):
            if not stack:
                stack.append((i, val))
                continue
            lastVal = stack[-1]
            while val > lastVal[1]:
                diff = i - lastVal[0]
                res[lastVal[0]] = diff
                stack.pop()
                if stack:
                    lastVal = stack[-1]
                else:
                    break
            stack.append((i,val))
        
        return res

        