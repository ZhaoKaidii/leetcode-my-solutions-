class Solution(object):
    def reversePrint(self, head):
        s=[]
        while head:
            s.append(head.val)
            head=head.next
        return s[::-1]
