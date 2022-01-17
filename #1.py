"""
Problem:
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

"""

from typing import List


def check_sum(arr: List[int], target: int) -> bool:
    prev = set()
    for elem in arr:
        if (target - elem) in prev:
            return True
        prev.add(elem)
    return False


if __name__ == "__main__":
    print(check_sum([10, 7], 17))
    print(check_sum([10, 15, 3], 17))
    print(check_sum([10, 11, 3, 4], 17))
    

"""
Output:

True
False
False 

"""

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
