class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        leftP = 1
        rightP = 1
        zeroIndex = []
        zeroNums = 0

        # first thing first traverse the list find the number of zeros, if more than
        # 1, then the entire ans list should be all zeros
        # if 1 zero, just find it out its index and calculate its product and return
        # zero at anywhere else

        for k in range(0, len(nums)):
            if nums[k] == 0:
                zeroNums += 1
                zeroIndex.append(k)

        match zeroNums:
            case 1:
                final_ans = 1
                # fking boundary check needed
                for l in range(0, zeroIndex[0]):
                    final_ans *= nums[l]
                for l in range(zeroIndex[0]+1, len(nums)):
                    final_ans *= nums[l]
                ans[zeroIndex[0]] = final_ans
                return ans
            case n if n > 1:
                return ans

        for i in range(1, len(nums)):
            rightP *= nums[i]

        # things change when there's 0 in the list

        # or this prob can be treated as a 'slide window' thing
        # by calculating the 'left prod' and 'right prod' of the element
        # but things could be once violated when current element is 0
        # and hence the left or right prod can't be inferred
        
        # add the first element in ans
        ans[0] = rightP

        # starts from the second element, so no boundary check needed
        for j in range(1, len(nums)):
            leftP *= nums[j-1]

            # zero division check needed
            rightP //= nums[j]
            ans[j] = (leftP * rightP)
        return ans