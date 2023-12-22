class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # Need To Optimise this solution

        if arr.index(max(arr)) == 0 or arr.index(max(arr)) == len(arr) - 1 or len(arr) < 3:
            return False
        
        going_down = False
        i = 0
        while not going_down:
            if arr[i] > arr[i+1]:
                going_down = True
            elif arr[i] == arr[i+1]:
                return False
            i += 1
        
        while going_down and i < len(arr) - 1:
            if arr[i] <= arr[i+1]:
                return False
            i += 1
            
        return going_down
        

