from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        result.append(path)

        def backtracking(nums, startIndex):
            nonlocal path
            if startIndex == len(nums):
                return

            for i in range(startIndex, len(nums)):
                sub = nums[i]
                path.append(sub)
                result.append(path[:])
                backtracking(nums, i + 1)
                path.pop()

        backtracking(nums, 0)
        return result

so = Solution()
input1 = [1,2,2]

res = so.subsets(input1)
print(res)