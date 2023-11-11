class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        sorted_arrival_times = sorted(people)
        flowers.sort() 
        
        bloom_counts = {}  
        bloom_end_times = []  

        flower_idx = 0
        for person_time in sorted_arrival_times:
            
            while flower_idx < len(flowers) and flowers[flower_idx][0] <= person_time:
                heapq.heappush(bloom_end_times, flowers[flower_idx][1])
                flower_idx += 1

            while bloom_end_times and bloom_end_times[0] < person_time:
                heapq.heappop(bloom_end_times)

            bloom_counts[person_time] = len(bloom_end_times)

        flower_counts = [bloom_counts[arrival_time] for arrival_time in people]

        return flower_counts  