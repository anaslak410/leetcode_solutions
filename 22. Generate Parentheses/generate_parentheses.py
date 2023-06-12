from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # have not solved this because it requires backtracking, once you are familiar with backtracking solve this
        init_perm = []
        result = set()

        for i in range(n-1):
            init_perm.append(")")
            init_perm.insert(0, "(")

        print(init_perm)
        permute(init_perm, output)

        return result

    def permute(perm, output):
        for i, para in enumerate(perm):
            if para == ')':
                new_para = '('
            else:
                new_para = ')'
            perm[i] = new_para

            for sub_para in perm:
                pass


if __name__ == "__main__":
    sol = Solution()
    sol.generateParenthesis(n=4)
    print(ord('('))
    print(ord(')'))
