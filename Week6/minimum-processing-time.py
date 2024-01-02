class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True)
        processorTime.sort()
        execution_times = []
        for i in range(0,len(tasks),4):
            execution_times.append(max(tasks[i:i+4]) + processorTime[i//4])
        return max(execution_times)