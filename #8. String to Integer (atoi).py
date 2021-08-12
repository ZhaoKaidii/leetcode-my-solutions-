class Solution(object):
    def myAtoi(self,s):
        ss=len(s)
        c,si,r，sc="0",1,0,1
        for i in range(ss):
                         if (s[i]==' '):
                                       if sc>1: 
                                              break
                                       else:
                                               continue
                         elif s[i]=='-':
                                       si=-1
                                       if sc>1:
                                              break
                                       else:
                                              sc=sc+1
                                              continue
                         elif s[i]=='+':
                                       si=1
                                       if sc>1:
                                               break
                                       else:
                                              sc=sc+1
                                              continue
                         elif s[i].isdigit():          
                                       c=c+s[i]
                                       sc=2
                                       r=int(c)*si
                         else:
                                       break
        if si==-1 and int(c)>=2**31: return -(2**31)                             
        if si==1 and int(c)>=(2**31)-1: return (2**31)-1
        return r 
