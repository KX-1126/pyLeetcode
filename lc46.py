from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtracking(nums,used):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if used[i] == 1:
                    continue
                path.append(nums[i])
                used[i] = 1
                backtracking(nums,used)
                path.pop()
                used[i] = 0

        used = [0 for _ in nums]
        backtracking(nums,used)
        return result

so = Solution()
input1 = [1,2,3]

res = so.permute(input1)
print(res)