class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        yx = list(zip(nums2, nums1))
        xsum = [(x, x + y) for y, x in yx]
        xsum.sort()
        xs = [x for x, _ in xsum]
        sums = [s for _, s in xsum]

        def RMQ(sums):
            n = len(sums)
            k = n.bit_length() + 1
            st = [[None for _ in range(n)] for _ in range(k)]

            for i in range(n):
                st[0][i] = sums[i]

            for p in range(1, k):
                for i in range(n):
                    nxt = i + (1 << (p - 1))
                    if nxt < n:
                        st[p][i] = max(st[p - 1][i], st[p - 1][nxt])
                    else:
                        st[p][i] = st[p - 1][i]

            def query(l, r):
                p = (r - l + 1).bit_length() - 1
                len_ = 1 << p
                return max(st[p][l], st[p][r - len_ + 1])

            return query

        rmq = RMQ(sums)

        yx.sort()
        ys = [y for y, _ in yx]
        sufmaxxs = list(reversed(list(accumulate([x for y, x in reversed(yx)], max))))

        ans = []
        for xq, yq in queries:
            indxy = bisect.bisect_left(ys, yq)

            if indxy == len(ys):
                ans.append(-1)
                continue
            maxx = sufmaxxs[indxy]
            if maxx < xq:
                ans.append(-1)
                continue
            rindxx = bisect.bisect_right(xs, maxx) - 1
            lindxx = bisect.bisect_left(xs, xq)
            if lindxx == len(xs):
                ans.append(-1)
                continue
            ans.append(rmq(lindxx, rindxx))

        return ans

