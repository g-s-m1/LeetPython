from itertools import zip_longest
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for i, j in zip_longest(word1, word2, fillvalue=""):
            result.append(i) 
            result.append(j)  
        return ''.join(result)