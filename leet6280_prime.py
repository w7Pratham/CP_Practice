def euler_flag_prime(n):
    # 欧拉线性筛素数
    # 说明：返回小于等于 n 的所有素数
    flag = [False for _ in range(n + 1)]
    prime_numbers = []
    for num in range(2, n + 1):
        if not flag[num]:
            prime_numbers.append(num)
        for prime in prime_numbers:
            if num * prime > n:
                break
            flag[num * prime] = True
            if num % prime == 0:  # 这句是最有意思的地方  下面解释
                break
    return prime_numbers


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = euler_flag_prime(right)
        primes = [x for x in primes if x>=left]
        ans = []
        m = len(primes)
        for i in range(m-1):
            x,y = primes[i], primes[i+1]
            if not ans or y-x<ans[1]-ans[0]:
                ans = [x,y]
        return ans if ans else [-1, -1]
