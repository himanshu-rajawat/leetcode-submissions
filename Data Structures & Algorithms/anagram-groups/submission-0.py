class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Brute force - Iterating and converting every word to a dictionary, and then comparing every dictionary with other to group, time complexity - o(n^2), space complexity - o(n)
        #Optimised - Create a dictionary of alphabates where a to z each correspond to a prime number and thus we will calculate multiplication for each word and than based on that we will put that in a dictionary where key is multiplication result and values and list that have that multiplication, time complexity - o(n*w), space complexity - o(n)
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        def first_n_primes(n):
            primes = []
            num = 2  # Start checking for prime numbers from 2
            while len(primes) < n:
                if is_prime(num):
                    primes.append(num)
                num += 1
            return primes
        
        first_26_primes = first_n_primes(26)
        # Alphabet from 'a' to 'z'
        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        
        # Create the mapping
        prime_mapping = dict(zip(alphabet, first_26_primes))

        result_dict = {}

        for word in strs:
            value = 1
            for char in word:
                value = value*prime_mapping[char]
            result_dict.setdefault(value, []).append(word)

        return result_dict.values()