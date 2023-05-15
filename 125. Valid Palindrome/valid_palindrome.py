class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(s)
        length = len(s)
        print(f"array length:{length}")
        if length % 2 == 0:
            print("string lenghth is even")
        else:
            print("string lenghth is odd")
            # s = s
        j = length - 1
        i = 0

        passed_middle = False
        while i < j:
            print(f"\ni: {i}, j:{j}")
            while (i >= j):
                left = ord(s[i])
                if (left > 90):
                    left = left - 32
                if ((65 <= left <= 90) | (48 <= left <= 57)):
                    print(f"The character i:{chr(left)} is an alphabet.")
                    break
                print(f"The character i:{chr(left)} is not an alphabet.")
                i = i + 1
                if (i >= j):
                    passed_middle = True
                    break

            if passed_middle:
                print("passed middle")
                break

            while (True):
                right = ord(s[j])
                if (right > 90):
                    right = right - 32
                if ((65 <= right <= 90) | (48 <= right <= 57)):
                    print(f"The character j:{chr(right)} is an alphabet.")
                    break
                print(f"The character J:{chr(right)} is not an alphabet.")
                j = j - 1
                if (j <= i):
                    passed_middle = True
                    break

            if passed_middle:
                print("passed middle")
                break
            if (right != left):
                print(
                    f"The characters i:{chr(right)},j:{chr(left)} are not equal")
                return False
                # break

            j = j - 1
            i = i + 1
        # print(i-1)
        # print(j-1)
        return True


if __name__ == "__main__":
    sol = Solution()
    # sol.isPalindrome(s="A man, a plan, a canal: Panama")
    # print(sol.isPalindrome(s="0P"))
    print(sol.isPalindrome(s="a."))
    # sol.isPalindrome(s="11112221111")
