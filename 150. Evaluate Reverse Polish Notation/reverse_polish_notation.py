from typing import List

# if value is operator, recurse function by adding next and one after value and return the result
# if value is operand, return value
# edge cases
# - only one operand in the list
# - only one operator in the list
#  how can this be solved with a stack? do not know, will do it with recursion


class Solution:
    def represents_int(self, s):
        try:
            int(s)
        except ValueError:
            return False
        else:
            return True

    def evalRPN(self, tokens: List[str], index=-1) -> int:
        # print(tokens)
        # print(f"value {tokens[index]}")
        value = tokens[index]
        if (self.represents_int(value)):
            # print(f"value, will return {value}")
            value = int(value)
            return value

        right_operand = self.evalRPN(tokens=tokens, index=index - 1)
        left_operand = self.evalRPN(tokens=tokens, index=index-2)

        match value:
            case "-":
                result = left_operand - right_operand
                # print(
                #     f"firs: {left_operand}, sec: {right_operand} result-: {result}")
                # return result
            case "+":
                result = left_operand + right_operand
                # print(
                #     f"firs: {left_operand}, sec: {right_operand} result+: {result}")
                # return result
            case "*":
                result = left_operand * right_operand
                # print(
                #     f"firs: {left_operand}, sec: {right_operand} result*: {result}")
                # return result
            case "/":
                result = int(left_operand / right_operand)
                # print(
                #     f"firs: {left_operand}, sec: {right_operand} result/: {result}")
            # case _:
                # print(
                #     f"impossible {value}, first, {left_operand}, second {right_operand}")
                # return result
        # print(f"new val {tokens[index]}")
        # tokens[index] = result
        # print(f"will delete {tokens[index-2]}")
        try:
            del tokens[index-2]
        except IndexError:
            pass
        try:
            # print(f"will delete {tokens[index-1]}")
            del tokens[index-1]
        except IndexError:
            pass
        # print(f"will delete {tokens[index-1]}")
        return result


if __name__ == "__main__":
    sol = Solution()
    la = [1, 2, 3, 4]
    del la[1]
    print("-11".isnumeric())
    # print(sol.evalRPN(["13", "5", "+"]))
    print(sol.evalRPN(["4", "13", "5", "/", "+"]))
    print(sol.evalRPN(["10", "6", "9", "3", "+",
          "-11", "*", "/", "*", "17", "+", "5", "+"]))

# post solution notes
# it would have been cleaner If a stack were used. going from left to right
