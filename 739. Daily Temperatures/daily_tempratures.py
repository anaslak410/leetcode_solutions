from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[-1], 0)]
        print(stack)
        result = [0] * len(temperatures)

        for i, temp in enumerate(reversed(temperatures[:-1]), start=1):
            while (True):
                print(stack[-1])
                leng = len(stack)
                if leng == 0:
                    result.insert(0, 0)
                    break
                elif (stack[- 1][0] < temp):
                    print(temp)
                    stack.pop()
                else:
                    print(f"will insert{temp}")
                    result.insert(0, abs(stack[-1][1] - i))
                    break
            stack.append((temp, i))
        print(result)


if __name__ == "__main__":
    solution = Solution()
    solution.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 900])

""" Post solution notes
This problem should be solved with a monotonic stack, similar to the "next greater" problem
but the distance between the number and the number that is greater than it should be taken into account.
"""
