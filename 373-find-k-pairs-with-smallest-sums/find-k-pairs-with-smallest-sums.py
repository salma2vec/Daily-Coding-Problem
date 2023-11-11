class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        visited = set()
        heap = []
        output = []

        heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.add("0@0")

        while len(output) < k and heap:

            # val = heappop(heap)
            total,i,j = heappop(heap)
            output.append((nums1[i], nums2[j]))

            if i + 1 < len(nums1) and (str(i+1)+"@"+str(j)) not in visited:
                heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add(str(i+1)+"@"+str(j))

            if j + 1 < len(nums2) and (str(i)+"@"+str(j+1)) not in visited:
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add(str(i)+"@"+str(j+1))

        return output        