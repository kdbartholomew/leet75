# -*- coding: utf-8 -*-
"""MoveZeros.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EjoXEOHa7tmRNJTmm_VinrdhL0LLZGjg
"""

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.



# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]


# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1


# Follow up: Could you minimize the total number of operations done?

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        position = 0

        # First pass: move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0 :
                nums[position] = nums[i]
                position += 1

        # Second pass: fill the remaining elements with zeros
        for i in range(position, len(nums)):
            nums[i] = 0

solution = Solution()
nums = [0, 1, 0, 3, 12]
solution.moveZeroes(nums)
print(nums)