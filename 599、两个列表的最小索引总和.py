"""
假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。

示例 1:
输入:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
输出: ["Shogun"]
解释: 他们唯一共同喜爱的餐厅是“Shogun”。

示例 2:
输入:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
输出: ["Shogun"]
解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。


"""


"""
步骤：
1、求两者交集
2、第一次遍历，找到索引最小的
3、第二次遍历，把索引最小对应餐厅加入结果中
"""
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l1=set(list1)
        l2=set(list2)
        l12=l1&l2
        res=[]
        tmp=float('inf')
        for i in l12:
            tmp=min(tmp,list1.index(i)+list2.index(i))
        for i in l12:
            if list1.index(i)+list2.index(i)==tmp:
                res.append(i)
        return res

