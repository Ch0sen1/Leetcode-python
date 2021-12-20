class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minDiff = float("inf")
        dic = defaultdict(list)
        arr.sort()
        
        for i in range(len(arr)-1):
            diff = abs(arr[i+1] - arr[i])
            dic[diff].append([arr[i], arr[i+1]])
            minDiff = min(minDiff, diff)
        
        return dic[minDiff]
        