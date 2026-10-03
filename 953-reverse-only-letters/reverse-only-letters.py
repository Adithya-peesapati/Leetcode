class Solution(object):
    def reverseOnlyLetters(self, s):
        a = list(s)

        i = 0
        j = len(s) - 1

        while i < j:

            if not a[i].isalpha():
                i+=1
            
            elif not a[j].isalpha():
                j-=1
            
            else:
                a[i],a[j] = a[j],a[i]
                i+=1
                j-=1
        
        return "".join(a)