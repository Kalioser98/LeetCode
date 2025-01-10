class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        winNum=0
        winSubstring=""
        start=0
        while start<len(s):
            dictionary={}
            for i in range(start, len(s)):
                key=s[i]
                if key in dictionary:
                    break
                else:
                    dictionary[key]=1
            if len(dictionary)>winNum:
                winNum=len(dictionary)
                winSubstring="".join(dictionary.keys())
            start += 1
        #print(winNum)
        #print(winSubstring)
        return winNum