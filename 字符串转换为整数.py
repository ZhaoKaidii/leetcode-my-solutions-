class Solution(object):
    def strToInt(self, str):
        ss=len(str)
        num=['0','1','2','3','4','5','6','7','8','9']
        c='0'
        si=1
        r=0
        sc=1
        for i in range(ss):
                         if (str[i]==' '):
                                       if sc>1: 
                                              break
                                       else:
                                               continue
                         elif str[i]=='-':
                                       si=-1
                                       if sc>1:
                                              break
                                       else:
                                              sc=sc+1
                                              continue
                         elif str[i]=='+':
                                       si=1
                                       if sc>1:
                                               break
                                       else:
                                              sc=sc+1
                                              continue
                         elif str[i] in num:          
                                       c=c+str[i]
                                       sc=2
                                       r=int(c)*si
                         else:
                                       break
        if si==-1 and int(c)>=2**31:
                                    r=-(2**31)                             
        elif si==1 and int(c)>=(2**31)-1:
                                    r=(2**31)-1
                                                                  
        return r
