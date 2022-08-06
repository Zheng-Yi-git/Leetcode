#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode.cn/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (36.90%)
# Likes:    5482
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 3M
# Testcase Example:  '"babad"'
#
# 给你一个字符串 s，找到 s 中最长的回文子串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "cbbd"
# 输出："bb"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成
# 
# 
#

# @lc code=start
from inspect import isroutine
def isRotate(s, i, j):
    _len = len(s)
    for k in range(i, (i + j) // 2 + 1):
        if s[k] != s[j - (k - i)]:
            return False
    return True

class Solution:
    def expandFromCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left+1, right-1
    def longestPalindrome(self, s: str) -> str:
        maxlen = 0
        maxstr = ""
        for i in range (len(s)):
            l1, r1 = self.expandFromCenter(s, i, i)
            l2, r2 = self.expandFromCenter(s, i, i+1)
            if r1 - l1 + 1 > maxlen:
                maxlen = r1 - l1 + 1
                maxstr = s[l1:r1+1]
            if r2 - l2 + 1 > maxlen:
                maxlen = r2 - l2 + 1
                maxstr = s[l2:r2+1]
        return maxstr
# @lc code=end

