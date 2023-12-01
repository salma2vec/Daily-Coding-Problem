class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        heap = []
        time = 0
        for duration, end in courses:
            if time + duration <= end:
                heapq.heappush(heap, -duration)
                time += duration
            elif heap and -heap[0] > duration:
                time += heapq.heappop(heap) + duration
                heapq.heappush(heap, -duration)
        return len(heap)        