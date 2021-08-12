class Solution(object):
    def deleteNode(self, head, val):
        if head.val==val: return head.next
        pre,cur=head,head.next
        while cur and cur.val!=val:
                pre,cur=cur,cur.next
        pre.next=cur.next
        return head
