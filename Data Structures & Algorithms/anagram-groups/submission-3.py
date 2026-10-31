class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use python built-in functions to hash strings
        def builtInHash(strs: str) -> tuple:
            ints = [0]*26
            for char in strs:
                ints[ord(char)-97] += 1
            return tuple(ints)
        
        dikt = {}
        for string in strs:
            key = builtInHash(string)
            if dikt.get(key):
                dikt[key].append(string)
            else:
                dikt[key] = [string]
        
        return list(dikt.values())