class Solution:
	@lru_cache(None)
	def winnerSquareGame(self, n: int) -> bool:
		if n == 0:
			return False
		i = int(math.sqrt(n))
		while i >= 1:
			if not self.winnerSquareGame(n - i * i):
				return True
			i -= 1
		return False
        