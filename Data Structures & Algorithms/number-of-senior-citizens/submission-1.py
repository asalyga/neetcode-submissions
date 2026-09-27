class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count_of_passagers = 0

        for number in details:
            age = number[11:13]
            if int(age) > 60:
                count_of_passagers += 1
        return count_of_passagers