from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = []
        leng = len(heights)

        for i in range(leng):
            height = heights[i]
            print(f"item index {i} height { height} ")
            if (result < height):
                result = height

            last_dis = 0
            while (stack and stack[-1][1] > height):
                print(stack)
                last = stack.pop()
                print(f"last item {last} will be popped")
                distance = (i) - last[0]

                area = distance * last[1]
                print(f"area {area}")
                last_dis = last[0]
                if result < area:
                    result = area
            stack.append((i + last_dis, height))

        while (stack):
            last = stack.pop()
            distance = (leng-1) - last[0]
            area = distance * last[1]
            if result < area:
                result = area

        return result


if __name__ == "__main__":
    s = Solution()
    s.largestRectangleArea(heights=[2, 1, 5, 6, 2, 3])
