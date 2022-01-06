class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for i, num in enumerate(heights):
            while stack and num >= heights[stack[-1]]:
                stack.pop()
            stack.append(i)
        return stack
        