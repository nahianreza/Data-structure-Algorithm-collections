class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        total = 0
        res = []
        for i in range(1,n):
            res.append(i)
            total += i
        res.append(total * -1)
        print(sum(res))
        return res

        