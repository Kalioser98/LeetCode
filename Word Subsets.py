from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        dictionary = Counter()
        for word in words2:
            word_count = Counter(word)
            for char, count in word_count.items():
                dictionary[char] = max(dictionary[char], count)
        result = []
        for word in words1:
            dictionaryTemp = Counter(word)
            if all(dictionary[char] <= dictionaryTemp[char] for char in dictionary):
                result.append(word)
        
        return result