class Solution(object):
    def swapNumbers(self, numbers):
        numbers[0]=numbers[1]+numbers[0]
        numbers[1]=numbers[0]-numbers[1]
        numbers[0]=numbers[0]-numbers[1]
        return numbers
