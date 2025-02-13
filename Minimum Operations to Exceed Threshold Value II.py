import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        nums.sort()
        contador=0
        if len(nums)==1:
            return 0
        else:
            while nums and nums[0] < k:
                minimo=heapq.heappop(nums)
                maximo=heapq.heappop(nums)
                newValor=minimo*2+maximo
                heapq.heappush(nums, newValor)
                contador+=1
        return contador
