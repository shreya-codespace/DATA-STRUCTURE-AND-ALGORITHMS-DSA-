class Solution:    
    def palindromeCheck(self, s):
        def helper (i,j):
            if i>=j:
              return True
            if s[i]!= s[j]:
              return False
            
            return helper(i+1,j-1)
        return helper (0,len(s)-1)
