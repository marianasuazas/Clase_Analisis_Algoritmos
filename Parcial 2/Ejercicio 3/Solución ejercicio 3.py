class Solution:
    def canJump(self, nums: List[int]) -> bool:

        """
        Complejidad Temporal: O(n)
        Complejidad Espacial: O(1)
        El algoritmo recorre el arreglo manteniendo el índice más lejano que se puede alcanzar y verifica si en algún momento se puede llegar al último índice.
        """

        max_reach = 0
        
        for i in range(len(nums)):

            if i > max_reach:
                return False

            max_reach = max(max_reach, i + nums[i])
            
        return True
