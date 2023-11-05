from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Find the starting gas station's index to complete a circuit.

        Args:
            gas (List[int]): List of gas at each station.
            cost (List[int]): List of gas costs to travel to the next station.

        Returns:
            int: The starting gas station's index, or -1 if no valid circuit can be completed.
        """
        n = len(gas)
        total_gas = 0
        current_gas = 0
        start_station = 0

        for i in range(n):
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]

            # If we run out of gas before reaching the next station, start over from the next station
            if current_gas < 0:
                current_gas = 0
                start_station = i + 1

        # If the total gas is non-negative, there is a valid circuit
        if total_gas >= 0:
            return start_station
        else:
            return -1

        