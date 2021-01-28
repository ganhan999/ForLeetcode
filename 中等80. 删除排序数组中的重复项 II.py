"""
给定一个增序排列数组 nums ，你需要在 原地 删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

"""



"""
我们使用两个变量，i 是遍历数组的指针，count 是记录当前数字出现的次数。count 的最小计数始终为 1。
"""
#大神做法1
class Solution(object):
    def removeDuplicates(self, nums):
        i, count = 1, 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                count += 1
                if count > 2:
                    nums.pop(i)
                    i -= 1
            else:
                count = 1
            i += 1
        return len(nums)




"""
1、我们使用了两个指针，i 是遍历指针，指向当前遍历的元素；j 指向下一个要覆盖元素的位置。
2、同样，我们用 count 记录当前数字出现的次数。count 的最小计数始终为 1。
3、我们从索引 1 开始一次处理一个数组元素。
4、若当前元素与前一个元素相同，即 nums[i]==nums[i-1]，则 count++。若 count > 2，则说明遇到了多余的重复项。
在这种情况下，我们只向前移动 i，而 j 不动。
5、若 count <=2，则我们将 i 所指向的元素移动到 j 位置，并同时增加 i 和 j。
6、若当前元素与前一个元素不相同，即 nums[i] != nums[i - 1]，说明遇到了新元素，则我们更新 count = 1，
并且将该元素移动到 j 位置，并同时增加 i 和 j。
7、当数组遍历完成，则返回 j。
"""
#大神做法2
class Solution(object):
    def removeDuplicates(self, nums):
        j, count = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j