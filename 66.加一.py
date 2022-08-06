#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# https://leetcode.cn/problems/plus-one/description/
#
# algorithms
# Easy (45.80%)
# Likes:    1039
# Dislikes: 0
# Total Accepted:    517.4K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3]'
#
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
# 
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
# 
# 
# 示例 2：
# 
# 
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
# 
# 
# 示例 3：
# 
# 
# 输入：digits = [0]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        _len = len(digits)
        add = 0
        if digits[_len - 1] == 9:
            digits[_len - 1] = 0
            add = 1
        else:
            digits[_len - 1] += 1
            return digits
        i = _len - 2
        while i >= 0:
            if digits[i] + add == 10:
                digits[i] = 0
                add = 1
                i -= 1
            else:
                digits[i] += add
                return digits
        return [1] + digits
# @lc code=end

