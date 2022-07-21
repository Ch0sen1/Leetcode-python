class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            prev = [0] + res[-1] + [0]
            cur = []
            for i in range(1, len(prev)):
                cur.append(prev[i]+prev[i-1])
            res.append(cur)
        return res
                