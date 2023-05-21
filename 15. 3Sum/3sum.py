from collections import Counter
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for index, value in enumerate(nums):
            l = 0
            r = len(nums) - 1

            while r > l:
                print(f"rdex: {r}, ldex: {l}, index: {index}")
                print(f"rvalue: {nums[r]}, lvalue: {nums[l]}, value: {value}")
                res = value + nums[l] + nums[r]
                print(f"res:{res}\n")

                if res > 0:
                    r = r - 1
                elif res < 0:
                    l = l+1
                else:
                    if (index != l) & (l != r) & (r != index):
                        print([value, nums[l], nums[r]])
                        j = [value, nums[l], nums[r]]
                        j.sort()
                        result.add(tuple(j))
                        r = r - 1
                    else:
                        break

        return [list(i) for i in result if i]


if __name__ == "__main__":
    # aa = {0}
    # counter1 = Counter([1, 2, 5, 9])
    # aa.add(counter1)
    # print(aa)
    # counter1.update([1, 3, 1])
    # print(counter1)
    # print(wa)
    # print(4 != 1, 3 != 2, 2 != 4)
    sol = Solution()
    # print(sol.threeSum(nums=[3, 0, -2, -1, 1, 2]))
    print(sol.threeSum(nums=[0, -2, -1, 1, 2]))
