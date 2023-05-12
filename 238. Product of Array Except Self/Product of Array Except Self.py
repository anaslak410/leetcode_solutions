from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        for i in range(500, 0):
            print(i)

        right_side_totals = {}
        # reversed_nums = list(reversed(nums))
        length = len(nums)

        total = 1
        for i in range(length - 1, -1, -1):
            total = nums[i] * total
            right_side_totals[i] = total

        # print(right_side_totals)
        totals = right_side_totals.copy()

        left_side_total = 1
        totals[0] = right_side_totals[1]

        for i in range(1, length - 1):
            left_side_total = left_side_total * nums[i-1]
            # print(left_side_total)
            totals[i] = right_side_totals[i+1] * left_side_total

        before_last_num = nums[length - 2]
        # last_num = nums[length - 1]

        totals[length-1] = left_side_total * before_last_num
        print(totals)
        result = list(totals.values())
        # result.reverse()
        print(result)
        return result


if __name__ == "__main__":
    sol = Solution()
    sol.productExceptSelf([1, 2, 3, 4])
