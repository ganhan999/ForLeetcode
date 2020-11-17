"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

说明：
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
 
示例：

输入：
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出：[1,2,2,3,5,6]
 

提示：
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n


"""
"""
思路分析：
用内置方法sort即可，注意要原地操作，不能改变地址，所以要使用对象类型方法例如pop，append，extend

"""
#我的做法1
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        lens=len(nums1)
        for i in range(lens-m):
            nums1.pop(-1)#不能直接切片
        nums1.extend(nums2)#不能使用nums1+nums2
        nums1.sort()
        for i in range(lens-len(nums1)):
            nums1.append(0)

# 我的做法2
#从nums2里面来一个，我就pop一个0。
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a=0
        popnum=0
        while nums2 != []:
           if a>=popnum+m:
               nums1.insert(a,nums2.pop(0))
               nums1.pop(-1)
               a+=1
           elif nums1[a]<=nums2[0]:
               a+=1
           else:
               nums1.insert(a,nums2.pop(0))
               nums1.pop(-1)
               a+=1
               popnum+=1

#大神做法1

"""
啊！我没有想到直接替换，打扰了。
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m+i]=nums2[i]
        nums1.sort()

#大神做法2

"""
充分利用了原数组的有序性，从后面开始比较，直接插入对应的那个位置。
"""
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


