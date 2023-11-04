class Solution:
    def countGoodStrings(self, low: int, high: int, z: int, o: int) -> int:
        # We cannot use a 2D array, so we'll use a hashtable.
        dp = dict()
        mod = 10**9 + 7

        def f(one=0, zero=0):
            # If the length is out of the range, return 0 and stop further computation.
            if one + zero > high:
                return 0

            # If the length is within the range, perform the operations.
            elif one + zero <= high:
                # If we've already computed this sub-problem, return the result directly.
                if zero + one in dp:
                    return dp[zero + one]
                else:
                    # Otherwise, calculate the number of valid strings by either adding '1' or '0'.
                    One_Add = f(one + o, zero)
                    Zero_Add = f(one, zero + z)
                    ADD_IF_GOOD = 1 if one + zero >= low else 0

                    # Memorize the answer and return it. Apply mod if the answer is large.
                    dp[zero + one] = (One_Add + Zero_Add + ADD_IF_GOOD) % mod
                    return dp[zero + one]

        return f()



        