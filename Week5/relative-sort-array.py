class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count_array = {}
        for index, num in enumerate(arr2):
            count_array[num] = index
        arr1.sort(key = lambda num:count_array.get(num, 1000 + num))
        return arr1