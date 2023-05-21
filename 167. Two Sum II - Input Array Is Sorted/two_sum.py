from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            return [1, 2]
        for index1, num1 in enumerate(numbers):
            upper = len(numbers) - 1
            lower = 0
            while (upper - 1 != lower):
                mid_index = lower + ((upper-lower)//2)
                print(mid_index)
                mid_num = numbers[mid_index]

                if (num1 + mid_num > target):
                    upper = mid_index
                else:
                    lower = mid_index
                if ((num1 + mid_num == target) & (index1 != mid_index)):
                    return [index1+1, mid_index + 1]
                if ((num1 + numbers[lower] == target) & (index1 != lower)):
                    return [index1+1, lower + 1]
                if ((num1 + numbers[upper] == target) & (index1 != upper)):
                    return [index1+1, upper + 1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum(numbers=[-12, 1, 5, 25, 75], target=100))
