from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First just find out the frequencies of all elements, put it into a 
        # dict, then sort it by frequency with length of k, bang, 
        # mision accopmlished

        # So the question is narrowed down to return the top k values in given
        # list within O(n), or one scan of the list

        len_n = len(nums)
        if len_n < k:
            return []

        set_nums = set(nums)
        len_s = len(set_nums)

        if len_s < k:
            return []
        elif len_s == k:
            return list(set_nums)

        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1

        # Linked list seems to be the better option?
        topK = [0] * k
        maxi, mini = 0, 0
        freqs = list(freq_dict.values())
        for freq in freqs:
            if freq > maxi:
                maxi = freq
                topK.pop()
                topK.insert(0, maxi)
                mini = topK[-1]
            elif freq > mini:
                # Within in the range, insertion could be done
                for index, value in enumerate(topK):
                    if freq > value:
                        topK.pop()
                        topK.insert(index, freq)
                        mini = topK[-1]
                        break
            
        res = []
        
        for key, value in freq_dict.items():
            if value in topK:
                res.append(key)

        return res
