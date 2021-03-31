"""
给出N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。
前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。

(注：分数越高的选手，排名越靠前。)

示例 1:
输入: [5, 4, 3, 2, 1]
输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal").
余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。

"""


"""
如果直接排序是不行的，因为会丢失老的索引。 因此我用了一个 pairs 数组，
来维护一个 nums -> 索引的映射。之后对 paris 进行降序排列即可。由于我事先保存了老的索引信息，因此是没有问题的。
"""
#大神做法1
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        pairs = []
        for i in range(len(nums)):
            pairs.append([nums[i], i])
        pairs.sort(key=lambda a: a[0], reverse=True)
        for i in range(len(nums)):
            if i == 0:
                nums[pairs[i][1]] = "Gold Medal"
            if i == 1:
                nums[pairs[i][1]] = "Silver Medal"
            if i == 2:
                nums[pairs[i][1]] = "Bronze Medal"
            if i > 2:
                nums[pairs[i][1]] = str(i + 1)
        return nums


