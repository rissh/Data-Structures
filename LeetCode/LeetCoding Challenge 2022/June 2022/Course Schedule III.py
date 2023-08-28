
import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        totalDays = 0
        maxHeap = []
        for i in range(len(courses)):
            totalDays += courses[i][0]
            heapq.heappush(maxHeap, -courses[i][0])
            if courses[i][1] < totalDays:
                courseWithMaxDuration = heapq.heappop(maxHeap)
                totalDays += courseWithMaxDuration
        return len(maxHeap)
      
