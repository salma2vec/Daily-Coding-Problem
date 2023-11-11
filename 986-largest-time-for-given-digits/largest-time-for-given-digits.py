class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        max_time = -1

        for h1, h2, m1, m2 in permutations(arr):
            hours = h1 * 10 + h2
            minutes = m1 * 10 + m2

            curr_time = hours * 100 + minutes

            if 0 <= hours <= 23 and 0 <= minutes <= 59 and curr_time > max_time:
                max_time = curr_time

        return "{:02d}:{:02d}".format(max_time // 100, max_time % 100) if max_time != -1 else ""