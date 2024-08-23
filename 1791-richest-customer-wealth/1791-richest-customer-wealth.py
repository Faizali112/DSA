class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        highest_sum = 0
        for account in accounts:
            current_sum = sum(account)
            if highest_sum < current_sum:
                highest_sum = current_sum

        return highest_sum