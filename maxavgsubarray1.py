# -*- coding: utf-8 -*-
"""maxAvgSubArray1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bOdW3DYDWxE9LEom0suQFeqd7tHC_4CC
"""

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.



# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000


# Constraints:

# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104

from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

#  ok so this works but its slow and i can do better.. see below
        startIndex = 0
        endIndex = k -1
        done = False
        i = 0
        maxSum = -1
        if len(nums) == k:
            ans = mean(nums)
            done = True
        while endIndex < len(nums):
            #calculate current mean
            i = startIndex
            currentSum = 0
            while i <= endIndex:
                currentSum = currentSum + nums[i]
                i = i + 1
            if currentSum > maxSum:
                maxSum = currentSum
            startIndex = startIndex + 1
            endIndex = endIndex + 1
        if endIndex == len(nums):
            done = True
            ans = maxSum / k
        if done == True:
            return ans

 # testing
solution = Solution()
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(solution.findMaxAverage(nums, k))  # expected output: 12.75 :) yay!

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

       #optimization: only consider how sliding the sum window over 1 element changes the sum...
       # (get rid of the start index value and consider the new end index value)
        startIndex = 0
        endIndex = k -1
        currentSum = sum(nums[startIndex: endIndex + 1]) #upperbound for slicing is exclusive
        maxSum = currentSum
        if len(nums) == k:
            ans = sum(nums)/k


        while endIndex < len(nums) - 1:
            #consider the current sum
            endIndex += 1
            currentSum = currentSum - nums[startIndex] + nums[endIndex]
            startIndex += 1
            if currentSum > maxSum:
                maxSum = currentSum
        return maxSum/k


# testing
solution = Solution()
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(solution.findMaxAverage(nums, k))  # expected output: 12.75 :) yay!