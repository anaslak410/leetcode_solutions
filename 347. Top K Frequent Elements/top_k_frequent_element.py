from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        result.append([0, 0])
        nums.sort()
        num_occurence = 1
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                print(
                    f"current num :{nums[i]} not equal to num before: {nums[i-1]}")

                for j in range(len(result)):
                    print(f"j = {j}")
                    if j + 1 > k:
                        print(f"{j} is bigger than {k}")
                        break

                    if result[j][1] > num_occurence:
                        print(
                            f"current num occ:{num_occurence} is smaller than: {result[j]}")
                        continue
                    else:
                        result.insert(j, [nums[i-1], num_occurence])
                        break

                num_occurence = 1
            else:
                print(
                    f"current num :{nums[i]} equal to num before: {nums[i-1]}")
                num_occurence = num_occurence + 1

        print(num_occurence)
        for j in range(len(result)):
            if j + 1 > k:
                break

            if result[j][1] > num_occurence:
                print(
                    f"current num occ:{num_occurence} is smaller than: {result[j]}")
                continue
            else:
                result.insert(j, [nums[len(nums) - 1], num_occurence])
                break

        print(result[:3])

        final_result = []
        for i in result[:k]:
            final_result.append(i[0])

        print(final_result)
        # for i in nums:
        #     if occur_map.setdefault(i) is None:
        #         occur_map[i] = 0
        #     else:
        #         occur_map[i] += 1

        # print(occur_map)
        # for i in occur_map:

        return final_result


if __name__ == "__main__":
    sol = Solution()
    sol.topKFrequent(nums=[1, 1, 2, 2, 5, 5, 5, 5, 8, 9, 9, 9, 9, 9, 9], k=1)
