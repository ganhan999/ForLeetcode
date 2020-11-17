from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 输入：
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 输出：[1,2,2,3,5,6]
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n:
            if m == 0:
                nums1[n-1] = nums2[n-1]
                n -= 1
                continue
            if nums1[m-1] < nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1




a=Solution()

a.merge([1,2,5,0,0,0,0],3,[4,5,6],3)

