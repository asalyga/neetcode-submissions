class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count_of_passagers = 0

        for number in details:
            if (int(number[11]) == 6 and int(number[12]) > 1)or (int(number[11]) > 6 and int(number[12]) >= 0):
                count_of_passagers += 1

        return count_of_passagers