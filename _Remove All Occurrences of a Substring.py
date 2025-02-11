import re
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = re.sub(part, "", s, count=1)
        return s