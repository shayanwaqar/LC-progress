class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre = [1] * len(nums)
        suf = [1] * len(nums)

        for i in range(1, len(nums)):
            pre[i] = nums[i-1] * pre[i-1]
            # [1,2,3,4]
            # [1,1,2,6]
        for i in range(len(nums)-2, -1, -1):
            suf[i] = nums[i+1] * suf[i+1]
            # [1,2,3,4]
            # [24,12,4,1]
        
        ret = [(pre[i]*suf[i]) for i in range(len(nums))]
        return ret





        # pre = [1]*len(nums) #pre = [1]
        # suf = [1]*len(nums)
        # rev = nums[::-1]
        
        # for i in range(1, len(nums)):
        #     pre[i] = pre[i-1] * nums[i-1]
        #     suf[i] = suf[i-1] * rev[i-1]
        # suf = suf[::-1]
        
        # ret = [1]*len(nums)
        # for i in range(len(nums)):
        #     ret[i] = pre[i] * suf[i]    
        # return ret