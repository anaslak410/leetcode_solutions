from typing import List


class Solution:

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """Find two indices in the list that when added up, equal the target"""
        firstIndex = None
        secondIndex = None

        # nums.sort()
        foundTarget = False

        startLocation = 0
        for i in range(len(nums)):
            # if (abs(nums[i]) > target & nums[i] > target):
            #     continue
            print(startLocation)

            for j in range(startLocation, len(nums)):
                if i == j:
                    continue
                if (nums[j] + nums[i] == target):
                    print("found target")
                    print(f"first number:  {nums[j]}  index: ", j)
                    print("second number: ", nums[i], " index: ", i)
                    print("sum of both numbers: ", nums[j] + nums[i], "\n")
                    firstIndex = j
                    secondIndex = i
                    foundTarget = True
                    break
            if foundTarget:
                break
            startLocation += 1

        return [firstIndex, secondIndex]


# def test_fun(a, b=4):
#     print(a)

name = 4
if __name__ == "__main__":
    solution = Solution()
    print("result: ", solution.two_sum([-1, -2, -3, -4, -5], -8))
    # test_fun(3, b=4)
