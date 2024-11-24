class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        return str1[:self.gcd(len(str1), len(str2))]
    
    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
        