"""
给定一个包含红色、白色和蓝色，一共n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。


示例 1：
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

示例 2：
输入：nums = [2,0,1]
输出：[0,1,2]

示例 3：
输入：nums = [0]
输出：[0]

示例 4：
输入：nums = [1]
输出：[1]

提示：
n == nums.length
1 <= n <= 300
nums[i] 为 0、1 或 2


"""


"""
单指针
我们可以考虑对数组进行两次遍历。在第一次遍历中，我们将数组中所有的 0 交换到数组的头部。
在第二次遍历中，我们将数组中所有的 11 交换到头部的 0 之后。此时，所有的 2 都出现在数组的尾部，这样我们就完成了排序。

"""
#大神做法1
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        ptr = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        for i in range(ptr, n):
            if nums[i] == 1:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1


"""
双指针，一个指向换0的位置，一个指向换1的位置
"""
#大神做法2
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0 = p1 = 0
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:#如果p0 < p1，要把nums[i], nums[p1]互换，当 p_0 < p_1时，我们已经将一些1连续地放在头部，此
                    # 时一定会把一个 11 交换出去，导致答案错误
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1

