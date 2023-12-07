class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        smaller_list = list1 if len(list1) < len(list2) else list2
        bigger_list = list2 if len(list1) < len(list2) else list1
        min_index_sum = len(list1) + len(list2) - 1
        
        for i in smaller_list:
            if i in bigger_list and list1.index(i) + list2.index(i) < min_index_sum:
                min_index_sum = list1.index(i) + list2.index(i)
                result = []
                result.append(i)
            
            elif i in bigger_list and list1.index(i) + list2.index(i) == min_index_sum:
                result.append(i)
        
        return result
        