class Solution:
    def reverseVowels(self, s: str) -> str:
        rev=[]
        result=[]
        for i in s:
            if i in('a','e','i','o','u','A','E','I','O','U'):
                rev.append(i)

        for char in s:
            if char in ('a','e','i','o','u','A','E','I','O','U'):
                result.append(rev.pop()) 
            else:
                result.append(char)
        
        return ''.join(result) 


        