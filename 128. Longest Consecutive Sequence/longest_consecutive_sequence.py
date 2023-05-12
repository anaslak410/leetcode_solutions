from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # not really correct, as this runs in n logn time complexity, question asks for n time complexity
        nums.sort()

        current_maks, maks = 1, 1

        for i in range(1, len(nums)):
            print(maks, current_maks)
            if nums[i] - 1 == nums[i-1]:
                current_maks = current_maks + 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                if current_maks > maks:
                    maks = current_maks
                current_maks = 1
        if current_maks > maks:
            maks = current_maks
            current_maks = 1
        print(nums)
        print(maks)
        return maks


if __name__ == "__main__":
    sol = Solution()
    sol.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
