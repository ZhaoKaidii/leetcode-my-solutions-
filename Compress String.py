class Solution(object):
    def compressString(self, S):
        ST=S+"0"
        st,i,j,c="",0,1,1
        while j<len(ST):
              if ST[j]==ST[i]:
                  c+=1
                  j+=1
              else:
                  st=st+ST[i]+str(c)
                  c=1
                  i=j
                  j+=1
        return st if len(st)<len(S) else S
