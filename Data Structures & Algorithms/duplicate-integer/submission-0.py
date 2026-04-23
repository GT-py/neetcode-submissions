class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        array = []
        for i in range(len(nums)):
            array.append(nums[i])
            for j in range(len(array)-1):
                if array[j] == nums[i]:
                    return True
        return False
