from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0

        output = 0
        length = len(height) - 1

        current_size = 0
        current_anchor = height[0]
        left_anchor_index = 0

        for left_index in range(1, length + 1):
            left_value = height[left_index]
            if (left_value >= current_anchor):
                output = current_size + output
                current_size = 0
                current_anchor = height[left_index]
                left_anchor_index = left_index
            else:
                current_size = (current_anchor - left_value) + current_size

        if (current_size != 0):
            current_size = 0
            current_anchor = height[length]
            for right_index in reversed(range(left_anchor_index, length)):
                right_value = height[right_index]
                if (right_value >= current_anchor):
                    output = current_size + output
                    current_size = 0
                    current_anchor = height[right_index]
                else:
                    current_size = (current_anchor -
                                    right_value) + current_size

        return output


if __name__ == "__main__":
    sol = Solution()
    print(sol.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(sol.trap(height=[4, 2, 3]))
    print(sol.trap(height=[2, 0, 2]))
    # print(sol.trap(height=[3, 2, 1, 2, 0, 0]))
