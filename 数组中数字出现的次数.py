class Solution(object):
    def singleNumbers(self, nums):
#定义一个函数用来计算整个数组的异或值
        def xo(f):
            h=0
            for i in range(len(f)):
                h=h^f[i]
            return h
 #定义一个函数用来将两个不重复的数字分到两个不同的数组           
        def div(c,d,f):
            s1,s2=[],[]
            for i in range(len(f)):
                g=f[i]^c
                g>>=d
                if g%2==1:
                    s1.append(f[i])
                else:
                    s2.append(f[i])
            return s1,s2
#正文，计算数组的异或值，利用该值将数组分为两组，分别计算两组的异或值
        c,d=xo(nums),0
        while c%2==0:
            c>>=1
            d=d+1
        s1,s2=div(c,d,nums)
        return [xo(s1),xo(s2)]
