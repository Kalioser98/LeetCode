class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maximo = 0  
        maximoTemp = nums[0]  

        for i in range(1, len(nums)): 
            if nums[i] > nums[i - 1]:  
                maximoTemp += nums[i]  
            else:  
                maximo = max(maximo, maximoTemp) 
                maximoTemp = nums[i] 
        
        maximo = max(maximo, maximoTemp)  
        return maximo
