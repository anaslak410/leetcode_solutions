

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (not s):
            return 0
        char_dict = {}
        length = 0
        longest_length = 0
        i = 0
        while True:
            print(f"current index {i}")
            char = s[i]
            print(f"current char: {char}")
            print(f"current length: {length}")
            print(f"current max length: {longest_length}")
            if char_dict.setdefault(char) is not None:

                if length > longest_length:
                    longest_length = length
                print(
                    f"character dictionary before modification : {char_dict}")
                for key in char_dict.copy():
                    if char_dict[key] < char_dict[char]:
                        length = length - 1
                        del char_dict[key]
                print(f"character dictionary after modification : {char_dict}")

            else:
                length = length + 1

            char_dict[char] = i

            if i >= len(s) - 1:
                break
            else:
                i = i + 1
            # print("\n")

        if length > longest_length:
            longest_length = length

        # print(char_dict)
        # print(f"current length: {length}")
        # print(longest_length)

        return longest_length


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("dvdf"))
    print(sol.lengthOfLongestSubstring("abcabcbb"))
