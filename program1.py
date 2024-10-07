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
                if b and b[-1]==a[i]:
                    b.pop()
                else:
                    return False
        return not b


    



  

