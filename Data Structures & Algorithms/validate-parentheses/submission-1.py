class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        opener = []

        for c in s:
            if c not in Map:
                opener.append(c)
            else:
                if not opener or opener[-1] != Map[c]:
                    return False
                opener.pop()
        return not opener
        