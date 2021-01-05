"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]

示例 2：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]



"""

"""

如果要比较两个列表是否一样，一个容易想到的办法是对列表分别排序，然后逐个比对。既然要排序，我们就可以 在搜索之前就对候选数组排序，一旦发现某个分支搜索下去可能搜索到重复的元素就停止搜索，这样结果集中不会包含重复列表。

    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
        continue



"""

#大神做法1
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path.copy())
                return
            for i in range(size):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:#还没被撤销的节点则可以构成一组完整的结，如果被撤销了那么就是重复的结。
                        continue
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth + 1, path, used, res)
                    used[i] = False
                    path.pop()
        size = len(nums)
        if size == 0:
            return []
        nums.sort()
        used = [False] * len(nums)
        res = []
        dfs(nums, size, 0, [], used, res)
        return res

