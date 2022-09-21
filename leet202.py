class Solution:
    def isHappy(self, n: int) -> bool:

        cac = set()
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            if n in cac:
                return False
            else:
                cac.add(n)
        return True
      
      
        # curr = n
        # curr_res = 0
        # while curr != 1:
        #     for i in str(curr):
        #         curr_res += int(i)**2
        #     curr = curr_res
        #     curr_res = 0
        # return True
