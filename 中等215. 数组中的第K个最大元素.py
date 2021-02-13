"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4



"""


"""
排序
"""
#大神做法1
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse = True)[k - 1]




"""
堆排序，库函数
"""
#大神做法2
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


"""
手写堆排序
"""
#大神做法3
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        寻找第k个大的元素第一想法是构建小顶堆
        '''

        def shift_up(new_idx):
            new_val = minheap[new_idx]  # 临时存储需要上浮的元素
            # 向上寻找父结点进行比较，决定是否上浮
            while new_idx > 0 and minheap[(new_idx - 1) // 2] > new_val:
                minheap[new_idx] = minheap[(new_idx - 1) // 2]  # 父结点下沉
                new_idx = (new_idx - 1) // 2  # 子结点坐标上移
            minheap[new_idx] = new_val  # 完成结点上浮

        def shift_down(start, end):
            start_val = minheap[start]  # 临时存储头节点
            # 向下寻找双子结点进行比较，决定是否下沉
            while start * 2 + 1 <= end:
                child = start * 2 + 1  # 设置左子节点
                # 比较左右子节点的大小，对于小顶堆来说，需要找出最小子结点
                if child + 1 <= end and minheap[child] > minheap[child + 1]:
                    child += 1
                if minheap[child] < start_val:
                    minheap[start] = minheap[child]  # 子结点上浮
                    start = child
                else:
                    break
            minheap[start] = start_val  # 完成结点下沉

        # 上浮式建堆
        minheap = []
        for i in range(min(len(nums), k)):
            minheap.append(nums[i])
            shift_up(i)

        # 下沉式维护
        for num in nums[k:]:
            if num > minheap[0]:
                minheap[0] = num
                shift_down(0, k - 1)

        return minheap[0]






"""
快速排序＋选择
"""
#大神做法4
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition( left, right):
            tmp = nums[left]
            while left < right:
                while left < right and nums[right] <= tmp:#注意是找大的，所以要从大到小排序
                    right = right - 1
                nums[left] = nums[right]
                while left < right and nums[left] >= tmp:
                    left = left + 1
                nums[right] = nums[left]
            nums[left] = tmp
            mid = left
            return mid

        left = 0
        right = len(nums) - 1
        while 1:
            idx = partition(left, right)
            if idx == k - 1:
                return nums[idx]
            if idx < k - 1:
                left = idx + 1
            if idx > k - 1:
                right = idx - 1