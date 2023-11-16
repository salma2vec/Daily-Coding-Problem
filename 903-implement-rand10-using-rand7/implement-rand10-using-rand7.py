# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        arr = [[1,2],[3,4],[5,6],[7,8],[9,10]]
        val1 = rand7()
        while val1 >= 6:
            val1 = rand7()
        val2 = rand7()
        while val2 >= 7:
            val2 = rand7()
        return arr[val1 - 1][val2 % 2]