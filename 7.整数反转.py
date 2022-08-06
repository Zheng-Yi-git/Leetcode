#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode.cn/problems/reverse-integer/description/
#
# algorithms
# Medium (35.34%)
# Likes:    3568
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 3M
# Testcase Example:  '123'
#
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 
# 如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：x = 123
# 输出：321
# 
# 
# 示例 2：
# 
# 
# 输入：x = -123
# 输出：-321
# 
# 
# 示例 3：
# 
# 
# 输入：x = 120
# 输出：21
# 
# 
# 示例 4：
# 
# 
# 输入：x = 0
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# -2^31 
# 
# 
#

# @lc code=start
class Solution:
    def isOutOfRange(self, x):
        if x % 10 == 0:
            return False
        res = x % 10 if x > 0 else -x % 10
        tmp = x / 10 if x > 0 else -x / 10
        if (tmp < 100000000):
            return False
        elif res > 2:
            return True
        elif res == 2 and tmp > 
        
    def reverse(self, x: int) -> int:
        if self.isOutOfRange(x):
            return 0
        else:
            sign = -1 if x < 0 else 1
            tmp = str(abs(x))[::-1]
            return int(tmp, 10) * sign
# @lc code=end

