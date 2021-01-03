"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""

"""
用回溯的模板做，建立树形结构

    1               2               3
2       3       1       3       1       2
3       2       3       1       2       1  


"""

#大神做法1
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def backtrack(path,nums):
            if not nums:
                self.res.append(path[:])
                return
            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(path, nums[:i]+nums[i+1:])#把除了自己的数字取掉
                path.pop()
        backtrack([],nums)
        return self.res


"""
见缝插针法，依次将每个数插入缝中
"""

#大神做法2
class Solution:
    def permute(self, nums):
        res = [[nums[0]]]
        tem = []
        n = len(nums)
        for i in range(1,n):
            for k in res:
                for j in range(len(k)+1):
                    k.insert(j,nums[i])#在索引为j的位置插入元素
                    tem.append(k[:])
                    k.pop(j)#删除索引为j的元素
            res=tem
            tem=[]
        return res


"""
利用动态维护数组，标记已经填过和待填的数组，这样就不用添加path了，当待填数字为0的时候就表示已经形成了一组有效的数组
"""

#大神做法3
class Solution:
    def permute(self, nums):
        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        res = []
        backtrack()
        return res