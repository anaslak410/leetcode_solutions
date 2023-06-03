from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # biggest_area = 0
        # height.sort()

        # for i, ivalue in enumerate(height):
        #     for j, jvalue in enumerate(height):
        #         x = abs(j - i)
        #         if (ivalue > jvalue):
        #             area = jvalue * x
        #         else:
        #             area = ivalue * x
        #         print(area)
        #         if (biggest_area < area):
        #             biggest_area = area
        biggest_area = 0
        left = 0
        right = len(height) - 1
        while (left < right):
            area = min(height[left] - height[right]) * abs(right - left)

        return biggest_area


if __name__ == "__main__":
    print(6 // 3)
    sol = Solution()
    print(sol.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
