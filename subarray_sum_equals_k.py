class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        if len(nums)==0:
            return 0
        rSum=0
        count=0
        res_map={}
        res_map[0]=1 #for first subarray k-0=k
        for i in range(len(nums)):
            rSum+=nums[i]
            
            compliment=rSum-k
            if compliment in res_map:
                count = count + res_map[compliment]
            if rSum in res_map:
                res_map[rSum]=res_map[rSum]+1
            else:
                res_map[rSum]=1
        return count
            
        
