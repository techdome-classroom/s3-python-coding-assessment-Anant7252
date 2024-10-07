class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a={
            ')': '(', 
            '}': '{',
            ']': '['
        }
        b=[]
        
        for i in s:
            if i in a.values():
                b.append(i)
            elif i in a:
                







    



  

