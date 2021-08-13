class Solution(object):
    def minimumPerimeter(self, neededApples):
        f=0
        for i in range(1,100000):
            f+=12*(i**2)
            if neededApples<=f:
                return i*8
