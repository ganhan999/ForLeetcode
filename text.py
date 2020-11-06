from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lens=len(nums)
        i=0
        if lens==0:
            return 0
        while i<=lens-1:
            if val in nums:
                inde=nums.index(val)
                print(inde)
                nums.pop(inde)
                print()
            else:
                i=i+1
        return len(nums)
a=Solution()
print(a.removeElement([1],1))