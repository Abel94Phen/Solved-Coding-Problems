class Solution:
    def smallestValue(self, n: int) -> int:
        def isPrime(n):
            d = 2
            while d*d <= n:
                if not n%d:
                    return False
                d += 1
            return True
        
        def prime_factors(n):
            hashmap = {}
            d = 2
            while d*d <= n:
                while n%d == 0:
                    hashmap[d] = 1 + hashmap.get(d, 0)
                    n //= d
                d += 1

            if n > 1:
                hashmap[n] = 1 + hashmap.get(n, 0)
            return hashmap

        if n == 4:
            return 4
        while not isPrime(n):
            representation = prime_factors(n)
            n = 0
            for num, freq in representation.items():
                n += num*freq
        return n
