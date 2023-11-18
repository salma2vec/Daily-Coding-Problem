class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}

        for rod in rods:
            copy_dp = dp.copy()

            for difference, taller in dp.items():
                if (difference + rod) in copy_dp:
                    copy_dp[difference + rod] = max(copy_dp[difference + rod], taller + rod)
                else:
                    copy_dp[difference + rod] = max(0, taller + rod)

                shorter = taller - difference
                new_difference = abs(shorter + rod - taller)
                new_taller = max(shorter + rod, taller)

                if new_difference in copy_dp:
                    copy_dp[new_difference] = max(copy_dp[new_difference], new_taller)
                else:
                    copy_dp[new_difference] = max(0, new_taller)

            dp = copy_dp

        result = dp[0]
        return result