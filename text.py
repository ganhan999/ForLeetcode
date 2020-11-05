from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        print(len(nums))
        if len(nums)==0 or len(nums)==1:
            return len(nums)
        else:
            while(i<len(nums)):
                if nums[i]==nums[i+1]:
                    nums.pop(i)
                    print(nums)
                    print(len(nums))
                else:
                    print("i:",i)
                    i=i+1
                if i>=len(nums)-1:
                    return len(nums)

a=Solution()
print(a.removeDuplicates([1]))