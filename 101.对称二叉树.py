#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode.cn/problems/symmetric-tree/description/
#
# algorithms
# Easy (58.02%)
# Likes:    2022
# Dislikes: 0
# Total Accepted:    643.2K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [1, 1000] 内
# -100 <= Node.val <= 100
# 
# 
# 
# 
# 进阶：你可以运用递归和迭代两种方法解决这个问题吗？
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if (not root) or (not (root.left or root.right)):
            return True
        if not (root.left and root.right):
            return False
        if root.left.val != root.right.val:
            return False
        q = queue.Queue()
        q.put(root.left)
        q.put(root.right)
        while not q.empty():
            lc = q.get()
            rc = q.get()
            if not (lc or rc):
                continue
            if not (lc and rc):
                return False
            if lc.val != rc.val:
                return False
            else:
                q.put(lc.left)
                q.put(rc.right)
                q.put(lc.right)
                q.put(rc.left)
        return True
# @lc code=end

