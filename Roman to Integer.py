import re
class Solution:
    def romanToInt(self, s: str) -> int:
        regex_patterns = {
        "CM": 900,
        "CD": 400,
        "XC": 90,
        "XL": 40,
        "IX": 9,
        "IV": 4,
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

        total = 0
        for roman, value in regex_patterns.items():
            matches = re.findall(roman, s)
            total += len(matches) * value
            s = s.replace(roman, "") 

        return total