
import heapq
from dataclasses import dataclass, field
from typing import List

@dataclass(order=True)
class MyTask:
    index: int = field(compare=False)
    enqueueTime: int
    processingTime: int = field(compare=False)

@dataclass()
class MyTaskScheduled:
    index: int
    processingTime: int
    def __lt__(self, other):
        if self.processingTime == other.processingTime:
            return self.index < other.index
        return self.processingTime < other.processingTime
    def __gt__(self, other):
        if self.processingTime == other.processingTime:
            return self.index > other.index
        return self.processingTime > other.processingTime

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        for i in range(len(tasks)):
            heapq.heappush(heap, MyTask(i, tasks[i][0], tasks[i][1]))
        clock = heap[0].enqueueTime # [0] is the smallest
        readyHeap = []
        result = []
        while len(heap) > 0 or len(readyHeap) > 0:
            while len(heap) > 0 and heap[0].enqueueTime <= clock:
                task = heapq.heappop(heap)
                heapq.heappush(readyHeap, MyTaskScheduled(task.index, task.processingTime))
            if len(readyHeap) == 0:
                clock = heap[0].enqueueTime
                continue
            taskToDo = heapq.heappop(readyHeap)
            result.append(taskToDo.index)
            clock += taskToDo.processingTime
        return result
        
