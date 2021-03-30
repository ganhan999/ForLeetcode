"""
给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

美式键盘 中：
第一行由字符 "qwertyuiop" 组成。
第二行由字符 "asdfghjkl" 组成。
第三行由字符 "zxcvbnm" 组成。

示例 1：
输入：words = ["Hello","Alaska","Dad","Peace"]
输出：["Alaska","Dad"]

示例 2：
输入：words = ["omk"]
输出：[]

示例 3：
输入：words = ["adsdf","sfd"]
输出：["adsdf","sfd"]


"""


"""
1.先将三行键盘分别存储在三个数组中
2.利用两次for循环判断字母是否在对应的数组中，分别设置三个计数器如果在对应的键盘数组则计数器加一
3.分别判断三个计数器的值是否和单词长度一样，如果有一个一样就说明这个单词的字母全部都在某一个键盘数组
"""
#大神做法1
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        array_1 = ["q","w","e","r","t","y","u","i","o","p","Q","W","E","R","T","Y","U","I","O","P"]
        array_2 = ["A","S","D","F","G","H","J","K","L","a","s","d","f","g","h","j","k","l"]
        array_3 = ["z","x","c","v","b","n","m","Z","X","C","V","B","N","M"]

        result = []
        for word in words:
            count_1 = 0
            count_2 = 0
            count_3 = 0
            for letter in word:
                if letter in array_1:
                    count_1 += 1
                if letter in array_2:
                    count_2 += 1
                if letter in array_3:
                    count_3 += 1
            if count_1==len(word) or count_2==len(word) or count_3 == len(word):
                result.append(word)
        return result



