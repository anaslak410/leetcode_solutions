class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_arr = [letter for letter in s]
        t_arr = [letter for letter in t]

        s_dict, t_dict = {}, {}

        for i in range(len(s_arr)):
            s_dict[s_arr[i]] = s_dict.get([s_arr[i]], 0) + 1
            t_dict[t_arr[i]] = t_dict.get([t_arr[i]], 0) + 1

        if s_dict == t_dict:
            return True

        return False


if __name__ == "__main__":
    sol = Solution()
    sol.isAnagram(s="anagram", t="nagaram")
