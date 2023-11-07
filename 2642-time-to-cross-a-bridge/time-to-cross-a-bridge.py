class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        left,right = [],[] # (-efficiency,-index,availableTime)
        for i in range(k):
            heapq.heappush(left,(-time[i][0]-time[i][2],-i,0))
        left0,right0 = [],[] # (availableTime,-index)
        timing = 0
        while n>0:
            while left and n>0 and (not right0 or timing<right0[0][0]):
                _,i,avail = heapq.heappop(left)
                timing = max(avail,timing)+time[-i][0]
                heapq.heappush(right0,(timing+time[-i][1],i))
                n -= 1
                self.updateLeft(timing,left,right,left0,right0,time,n)
            self.updateRight(timing,left,right,left0,right0,time,n)
            while right:
                _,i,avail = heapq.heappop(right)
                timing = max(avail,timing)+time[-i][2]
                heapq.heappush(left0,(timing+time[-i][3],i))
                self.updateLeft(timing,left,right,left0,right0,time,n)
                self.updateRight(timing,left,right,left0,right0,time,n)
        return timing

    def updateLeft(self,timing,left,right,left0,right0,time,n):
        while left0 and (left0[0][0]<=timing or (not left and not right and right0 and left0[0][0]<right0[0][0]) or (not left and not right and not right0)):
            avail,i = heapq.heappop(left0)
            heapq.heappush(left,(-time[-i][0]-time[-i][2],i,max(avail,timing)))

    def updateRight(self,timing,left,right,left0,right0,time,n):
        while right0 and (right0[0][0]<=timing or (not right and (n==0 or not left))):
            avail,i = heapq.heappop(right0)
            heapq.heappush(right,(-time[-i][0]-time[-i][2],i,max(avail,timing)))