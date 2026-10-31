class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                    47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        def betHash(string: str, primes: List[int]) -> int:
            res = 1
            for char in string:
                res *= primes[ord(char)-97]
            return res

        dikt = {}

        for string in strs:
            key = betHash(string, primes)
            if dikt.get(key):
                dikt[key].append(string)
            else:
                dikt[key] = [string]

        return list(dikt.values())
        