from typing import List

class Solution:
    def mySqrt(self, x: int) -> int:
        low=0
        high=x
        while low<=high:
            mid=(low+high)//2
            if mid**2<=x:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
a=Solution()

print(a.mySqrt("1110","111"))