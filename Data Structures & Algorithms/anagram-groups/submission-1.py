class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # The key is to find out a way to hash the anagram into a unique value
        # So far I have no idea how to avoid hash collision

        # Now the problem is converted into hash the list of 26 numbers, 
        # in the hash function, their values and indices matter
        # + - * / // % ** abs() & | ^ ! 
        # value ^ (-(index+1)) = sth
        # sth * float(value+1/value+2)
        # for a single element
        # then sum them up

        def peteHash(string:str) -> float:
            ints = [0] * 26
            for char in string:
                ints[ord(char)-97] +=1

            res = 0.0
            for index, val in enumerate(ints):
                res += ((val ^ (-(index + 1))) * float((val + 1) / (val + 29)))
            return res
        
        dikt = {}

        for string in strs:
            key = peteHash(string)
            if dikt.get(key):
                dikt[key].append(string)
            else:
                dikt[key] = [string]

        return list(dikt.values())



