class Solution(object):
    def add(self, a, b):
        s=0
        for i in range(32):
            c=1<<i 
            if c&a!=0 and c&b!=0:
                k=1<<(i+1)
            else:
                f=(c&a!)|(c&b!)|k
            s=s|f
        return s
