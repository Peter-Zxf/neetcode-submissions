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
    # basically just calculate every "right prod" at corrsponding index
    # and store it in an
    # array, and use the result directly, hence in O(n) and no division used?

        rightProds = [1] * len(nums)
        tempRightP = 1
        for i in range(len(nums)-1, 0, -1):
            tempRightP *= nums[i]
            rightProds[i-1] = tempRightP

        ans[0] = rightProds[0]

        for i in range(1, len(nums)):
            leftP *= nums[i-1]
            ans[i] = leftP * rightProds[i]

        return ans