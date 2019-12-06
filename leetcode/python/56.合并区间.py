#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (39.16%)
# Likes:    223
# Dislikes: 0
# Total Accepted:    40.4K
# Total Submissions: 102.9K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 给出一个区间的集合，请合并所有重叠的区间。
# 
# 示例 1:
# 
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
# 
# 示例 2:
# 
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 
#

# @lc code=start
class Solution:
    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        """排序"""
        intervals = sorted(intervals, key= lambda interval: interval[0])
        res = [intervals[0]]
        for ele in intervals:
            if res[-1][1] >= ele[0]:
                res[-1][1] = ele[1] if ele[1] > res[-1][1] else res[-1][1]
            else:
                res.append(ele)
        return res
        
# @lc code=end

