class Solution(object):
    def canJump(self, nums):
        farthest = 0
        target = len(nums) - 1
        
        for i, jump_distance in enumerate(nums):
            if i > farthest:
                return False

            farthest = max(farthest, i + jump_distance)
            
            if farthest >= target:
                return True
                
        return farthest >= target