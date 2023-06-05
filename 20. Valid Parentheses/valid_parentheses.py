import unittest


class Solution:
    class Stack:
        pass

    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if (len(stack) == 0):
                stack.append(char)
                continue
            last = stack[len(stack) - 1]
            if (last == '(' and char == ')'):
                stack.pop()
            elif (last == '[' and char == ']'):
                stack.pop()
            elif (last == '{' and char == '}'):
                stack.pop()
            else:
                stack.append(char)

        if len(stack) == 0:
            return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print(ord(')'))
    print(ord('('))
    print(ord(']'))
    print(ord('['))
    print(ord('}'))
    print(ord('{'))
    print(sol.isValid(s="()[]{}") == True)
    print(sol.isValid(s="()") == True)
    print(sol.isValid(s="(}") == False)
    print(sol.isValid(s="(({(") == False)
    print(sol.isValid(s="(({(") == False)
    print(sol.isValid(s="(") == False)
    print(sol.isValid(s="[()]") == True)
    print(sol.isValid(s="(){}}{") == False)
