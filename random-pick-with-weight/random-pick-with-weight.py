class Solution:
	def __init__(self, w: List[int]):
		for i in range(1, len(w)):
			w[i] += w[i-1]
		self.presum = w

	def pickIndex(self) -> int:
		r = random.randint(1, self.presum[-1])
		lo, hi = 0, len(self.presum)-1
		while lo < hi:
			mid = (lo + hi) // 2
			if self.presum[mid] < r:
				lo = mid + 1
			else:
				hi = mid
		return lo
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()