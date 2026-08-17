class Solution:
    def shipWithinDays(self, weights, days):
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2

            reqdays = 1
            current_load = 0

            for weight in weights:
                if current_load + weight > mid:
                    reqdays += 1
                    current_load = 0

                current_load += weight

            if reqdays <= days:
                right = mid - 1
            else:
                left = mid + 1

        return left