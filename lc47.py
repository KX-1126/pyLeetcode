from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtracking(nums,used):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if used[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i-1] and used[i-1] == 0:
                    continue
                path.append(nums[i])
                # print(path)
                used[i] = 1
                backtracking(nums,used)
                path.pop()
                used[i] = 0

        nums.sort()
        used = [0 for _ in nums]
        backtracking(nums,used)
        return result

so = Solution()
input1 = [1,1,1,2,2]

f = so.permuteUnique(input1)
print(f)