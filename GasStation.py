class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas, tank, start = 0, 0, 0

        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            tank += gas[i] - cost[i]

            if tank < 0:  # means there is not enough gas to go to the next station
                tank = 0  # reset the tank to 0
                start = i + 1  # this will be the new start position

        return -1 if (total_gas < 0) else start