"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

 

示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

示例 2：
输入：nums = [0]
输出：[[],[0]]
 


提示：
1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同




"""


"""
库函数
"""
#大神做法1
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)+1):
            for tmp in itertools.combinations(nums, i):
                res.append(tmp)
        return res


"""
迭代
"""
#大神做法2
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for num in nums:
            res=res+[[num]+i for i in res]
        return res


"""
回溯
"""
#大神做法3
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # 存储符合要求的子集
        tmp = []
        n = len(nums)
        def helper(idx):
            # 先添加子集
            ans.append(tmp[:])
            for i in range(idx, n):
                tmp.append(nums[i])
                # 避免重复，每次递归，从下一个索引开始
                helper(i + 1)
                # 回溯
                tmp.pop()
        helper(0)
        return ans


"""
位运算，那一位是1就把那一位对应的值加进去
"""
#大神做法4
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        n = 1 << size
        res = []
        for i in range(n):
            cur = []
            for j in range(size):
                if i >> j & 1:
                    cur.append(nums[j])
            res.append(cur)
        return res