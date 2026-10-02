class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        summary = 0
        for op in operations:
            if op == "+":
                first = stack.pop()
                second = stack.pop()
                summed = first + second
                stack.append(second)
                stack.append(first)
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
                stack.append(int(op))
                summary += int(op)
        return summary
