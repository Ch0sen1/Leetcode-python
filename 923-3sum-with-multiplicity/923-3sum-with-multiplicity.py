class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        ans = 0
        
        for i in range(2 ,len(arr)):
            l = 0
            r = i - 1
            while l < r:
                total = arr[i] + arr[l] + arr[r]
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    lcount = 1
                    rcount = 1
                    while l + lcount < r and arr[l] == arr[l+lcount]:
                        lcount += 1
                    while l + lcount <= r - rcount and arr[r] == arr[r-rcount]:
                        rcount += 1
                    ans += (lcount + rcount) * (lcount + rcount - 1) // 2 if arr[l] == arr[r] else lcount * rcount
                    l += lcount
                    r -= rcount
        
        return ans % (10**9 + 7)
                
                
                
        