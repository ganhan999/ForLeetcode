"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。


示例 1:
输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

示例 2:
输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。


"""


"""
如果某一个作为 起跳点 的格子可以跳跃的距离是 3,那么表示后面 3 个格子都可以作为 起跳点。
可以对每一个能作为 起跳点 的格子都尝试跳一次，把能跳到最远的距离 不断更新。
如果可以一直跳到最后，就成功了。

"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_distance = 1#至少为1
        length = len(nums)
        index = 0

        while index+1 <= max_distance:#因为索引肯定要少1的
            max_distance = max(max_distance, nums[index] + index+1)
            if max_distance >= length:
                return True
            else:
                index += 1
        return True if index >= length else False



"""
同上
贪心算法
刷新每次最长距离
"""
#大神做法2
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 1
        for i in range(n):
            if i+1 <= rightmost:
                rightmost = max(rightmost, i +1 + nums[i])
                if rightmost >= n :
                    return True
        return False
