from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i
            else:
                result = [dict[target-nums[i]],i]
                return result




        # for i in nums:  # i 是 数值 不是下标
        #     j = target - i
        #     start_index = nums.index(i)
        #     next_index = start_index +1
        #     temp_nums = nums[next_index:]
        #     if j in temp_nums:
        #         print(i)
        #         result = [nums.index(i),next_index+temp_nums.index(j)]
        #         return result

        # n = len(nums)
        # for i in range(0,n):
        #     start_value = nums[i]
        #     other_value = target - start_value
        #     temp_nums =nums[i+1:]
        #     if other_value in temp_nums:
        #         result = [i, i+1+temp_nums.index(other_value)]
        #         return  result



if __name__ == "__main__":
    solution = Solution()
    # result = solution.twoSum([2, 7, 11, 15],9)
    result = solution.twoSum([3,3],6)
    print(result)

