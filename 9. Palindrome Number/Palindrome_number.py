class Solution:
    def isPalindrome(self, x: int) -> bool:
        numString = str(x)
        length = len(numString)

        index = int(length/2)
        if length % 2 != 0:
            numString = numString[:index] + numString[index+1:]

        if numString[:index] == numString[index:][::-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    sol.isPalindrome(1234567)
