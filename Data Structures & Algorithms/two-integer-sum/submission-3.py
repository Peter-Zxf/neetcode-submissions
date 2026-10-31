class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # assume there is always solution to the question
        length = len(nums)
        expanded = nums[:]
        for num in nums:
            expanded.append(target - num)
        # now the question is converted to such:
        # in a series of nums, there's only one duplicated num
        # the solution of this question is to find the duplicated num, in list 
        # expanded, and return the indicies of duplicated in both lists

        """print("nums: ", nums)
        print("expanded: ", expanded)
        """
        dikt = {}
        for i in range(len(expanded)):
            j = expanded[i]
            if dikt.get(j, 0) == 0:
                dikt[j]=1
            elif dikt.get(j, 0) == 1:
                if i < length:
                    return [nums.index(j), i]
                elif j*2 == target:
                    continue
                else:
                    """print("i:",i)
                    print("length:",length)
                    print("i-length:",i-length)
                    print("index:",nums.index(j))
                    try:
                        k = nums.index(j)
                    except Exception as e:
                        print(f"Here's error msg:{e}")
                    else:
                        print("Here we are")"""
                    return [i-length, nums.index(j)]
                """if j*2 == target:
                    try:
                        k = nums.index(j, i+1)
                    except ValueError:
                        dikt[j] = 0
                    else:
                        return [i, k]
                else:
                    return [i - length, nums.index(j)]"""
        # print("duplicate: ", j)
        # print("dikt: ", dikt)
        """if duplicate*2 != target:
            return [expanded.index(duplicate, length) - length, nums.index(duplicate)]
        else:
            # when target is twice as an element, there may be two answers
            pos = expanded.index(duplicate)
            return [pos, expanded.index(duplicate, pos+1)]"""

        # This doesn't work when target is twice as an element