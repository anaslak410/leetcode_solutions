class Solution:
    def groupAnagrams(self, strs):
        # we create a dict that contains all of them, what should keys be?
        # we need a way to quickly identify them,
        # key will be sorted palindrome

        anag_dict = {}
        for anag in strs:

            sorted_anag = self.get_sorted_anagram(anag)

            if anag_dict.setdefault(sorted_anag) is None:
                anag_dict[sorted_anag] = [anag]
            else:
                anag_dict[sorted_anag].append(anag)

        print(list(anag_dict.values()))
        return list(anag_dict.values())

    def get_sorted_anagram(self, anagram):
        return "".join(sorted(anagram))

    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False

    #     s_arr = [letter for letter in s]
    #     t_arr = [letter for letter in t]

    #     s_arr.sort()
    #     t_arr.sort()

    #     for i in range(len(s_arr)):
    #         if s_arr[i] != t_arr[i]:
    #             return False
    #     return True


if __name__ == "__main__":
    sol = Solution()
    sol.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])
    # sol.get_sorted_anagram("sldkfjsdlkfjs")
