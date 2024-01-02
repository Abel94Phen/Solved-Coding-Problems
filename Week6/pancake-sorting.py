class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        last = len(arr)
        K = []
        while last > 0:
            index = arr.index(max(arr[:last]))
            if index == 0:
                arr[:last] = arr[:last][::-1]
                K.append(last)
            else:
                arr[:index + 1] = arr[:index + 1][::-1]
                arr[:last] = arr[:last][::-1]
                K.append(index + 1)
                K.append(last)
            last -= 1
        return K