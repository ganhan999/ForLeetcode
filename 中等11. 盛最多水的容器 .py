"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器。

示例 1：
输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例 2：
输入：height = [1,1]
输出：1

示例 3：
输入：height = [4,3,2,1,4]
输出：16

示例 4：
输入：height = [1,2,1]
输出：2

"""


"""
暴力法

"""
#我的做法

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                res=max(res,(j-i)*min(height[i],height[j]))
        return res


#大神做法1

"""
双指针法
首先写下一个测试例子， 8 1 1 1 11 9 13 15 10 12

观察数据找规律。随便看一个范围比如【11...12】，能否找到比这更好的解？那么我们发现9肯定不能是左边的板，因为9本来就比11矮，还靠12更近，那【9...12】的面积肯定要更小啊，13倒是有可能！

规律：只有从最左开始升序的数字才可能是左板！【8】 1 1 1 【11】 9 【13】【15】10 12， 
不在【】里的统统不可能是左板。 同理，只有从最右开始升序的数字才可能是右板！
8 1 1 1 11 13 【15】 10 【12】

有了第三步的规律，其实离答案已经很近了：
【8】 1 1 1 【11】 9 【13】【15】 10 12 可能的左板在【】里
8 1 1 1 11 9 13 【15】 10 【12】 可能的右板在【】里
我们从最左边开始向右遍历可能的左板(8->11->13->15)，从最右边开始向左遍历可能的右板(12->15)
开始是【8...12】，面积是8*9=72

那接下来到底是从左往右的8->11呢还是从右往左的12->15呢？如果是12->15，
那明显面积是变小了；而8->11,面积可能增大！所以我们每次选择较短的板，
往左（或右）移，记录面积，直到左右碰头为止。

正确性：按照上面的思路下来，正确性就很明显了。

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res

