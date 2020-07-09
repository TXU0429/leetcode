class Solution():
    '''
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:

        Given nums = [2, 7, 11, 15], target = 9,
        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
    '''

    def twoSum(self, nums: list, target: int) -> list:
        '''
        :param nums: an array of integers
        :param target: an integer
        :return: indices of the two numbers such that they add up to a specific target
        '''
        dic = {}
        for idx, num in enumerate(nums):
            if num in dic:
                return [dic[num], idx]
            else:
                dic[target - num] = idx

aaaaaaaaaaaaaaaaaaaaaaaaaaaa

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    result = [0, 1]
    solution = Solution()
    answer = solution.twoSum(nums, target)
    assert len(answer) == len(result), f'Your answer is {answer}, should be {result}'
    assert all([True if answer[i] == result[i] else False
                for i in range(len(result))]), f'Your answer is {answer}, should be {result}'
    print('Pass test!')
