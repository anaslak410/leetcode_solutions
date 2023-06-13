from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result = 1
        leng = len(position)
        distances = [(0, 0)] * leng

        for i in range(leng):
            pos = position[i]
            dist_left = (target - pos)/speed[i]
            distances[i] = ((pos, dist_left))

        distances.sort(key=lambda a: a[0])

        front = distances[leng-1][1]
        for j in reversed(range(0, leng-1)):
            current = distances[j][1]
            if not (front >= current):
                front = current
                result = result + 1

        return result


"""
appraoches:
- can solve this with a stack according to neetcode. Dont know how though.
- go through cars in sorted order maybe.
- all positions are unique.
- has to be sorted
- If a car before a car cant catchup to it, then none of the cars ever can,
- if the one in front has less instances

Post solution thoughts:
- The stack solution by neetcode seemed to unneccesarily use a stack. It also has the same complexity as my solution. 

"""


if __name__ == "__main__":
    a = [0] * 10
    print(len(a))
    print(a)
    # sol = Solution()
    # sol.generateParenthesis(n=4)
