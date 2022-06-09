#167. Two Sum II - Input Array Is Sorted
#Ref_https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict = {}
        
        for ind, elem in enumerate(numbers):
            ind += 1
            rem = target - elem
            if rem in num_dict:
                return [num_dict[rem], ind]
            else:
                num_dict[elem] = ind
