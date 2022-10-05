class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

    sum = 0
    l = len(arr)

    for i in range(l):

        for j in range(i, l, 2):
            for k in range(i, j + 1, 1):
                sum += arr[k]

    return sum

""" Approach 2 """
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        sum = 0
        l = len(arr)

        for i in range(l):

            sum += ((((i + 1) * (l - i) + 1) // 2) * arr[i])

        return sum
