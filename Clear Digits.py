from collections import deque
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = deque()
        for i in range(len(s)):
            if s[i].isalpha():
                stack.append(s[i])
            elif s[i].isdigit():
                stack.pop()
        return ''.join(stack) 