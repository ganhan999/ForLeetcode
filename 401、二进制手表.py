"""
二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。

每个 LED 代表一个 0 或 1，最低位在右侧。


"""


"""
为了方便计算，分别设置了小时数组和分钟数组
递归的四个参数分别代表：剩余需要点亮的灯数量，从索引index开始往后点亮灯，当前小时数，当前分钟数
每次进入递归后，先判断当前小时数和分钟数是否符合要求，不符合直接return
for循环枚举点亮灯的情况，从index枚举到10，每次枚举

"""
#大神做法1
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        hours = [1, 2, 4, 8, 0, 0, 0, 0, 0, 0]
        minutes = [0, 0, 0, 0, 1, 2, 4, 8, 16, 32]
        res = []

        def backtrack(num, index, hour, minute):
            if hour > 11 or minute > 59:
                return
            if num == 0:
                res.append('%d:%02d' % (hour, minute))
                return
            for i in range(index, 10):
                backtrack(num - 1, i + 1, hour + hours[i], minute + minutes[i])

        backtrack(num, 0, 0, 0)
        return res
