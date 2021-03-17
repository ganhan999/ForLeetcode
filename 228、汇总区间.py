"""
给定一个无重复元素的有序整数数组 nums 。

返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。

列表中的每个区间范围 [a,b] 应该按如下格式输出：

"a->b" ，如果 a != b
"a" ，如果 a == b


示例 1：
输入：nums = [0,1,2,4,5,7]
输出：["0->2","4->5","7"]
解释：区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

示例 2：
输入：nums = [0,2,3,4,6,8,9]
输出：["0","2->4","6","8->9"]
解释：区间范围是：
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

示例 3：
输入：nums = []
输出：[]

示例 4：
输入：nums = [-1]
输出：["-1"]

示例 5：
输入：nums = [0]
输出：["0"]




"""


"""
双指针
一个指向区间最后一个，一个指向区间第一个
一当发现不符合，把前面指针指向后面指针
"""
#大神做法1
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        # 初始化双指针均指向数组头部
        left = 0
        right = 0
        ans = []
        # 开始遍历
        while right < n:
            # 数组有序
            # 先限定边界，查找间隔大于 1 的部分
            while right < n - 1 and nums[right] + 1 == nums[right + 1]:
                right += 1
            # 找到间隔之后，将前面连续部分按照规定格式添加到结果列表中
            tmp = [str(nums[left])]
            if nums[left] != nums[right]:
                tmp.append('->')
                tmp.append(str(nums[right]))
            ans.append(''.join(tmp))
            # 维护更新 right 和 left
            right += 1
            left = right
        return ans
