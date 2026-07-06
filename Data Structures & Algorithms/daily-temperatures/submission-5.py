class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, current in enumerate(temperatures):
            while stack and current > temperatures[stack[-1]]:
                prev = stack.pop()
                answer[prev] = i - prev
            stack.append(i)
        return answer
        