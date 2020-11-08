from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort(reverse=False)
            return nums.index(target)
a=Solution()
print(a.searchInsert([1,3,5,6],7))