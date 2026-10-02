class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        summary = 0
        for op in operations:
            if op == "+":
                first, second = stack[-1], stack[-2]
                summed = first + second
                stack.append(summed)
                summary += summed
            elif op == "D":
                last_score = stack[-1] * 2
                stack.append(last_score)
                summary += last_score
            elif op == "C":
                removed = stack.pop()
                summary -= removed
            else:
                val = int(op)
                stack.append(val)
                summary += val
        return summary
