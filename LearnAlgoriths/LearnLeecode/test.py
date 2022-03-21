class Solution(object):
    @classmethod
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        sort_nums = sorted(enumerate(nums), key=lambda x: x[1])
        sort_pure_nums = [x[1] for x in sort_nums]
        sort_pure_indexes = [x[0] for x in sort_nums]
        
        for index, num in enumerate(sort_pure_nums):
            try:
                find_result =  sort_pure_nums.index(target-num, index+1)
            except ValueError:
                find_result = -1
                
            if find_result != -1:
                return [sort_pure_indexes[find_result], sort_pure_indexes[index]]
        return []

print(Solution.twoSum(nums = [3,2,3], target = 6))