class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 待完善。。
# 要注意，交点不是数值相等，而是指针相等!!!!!
# 双指针解法
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # A, B = headA, headB
        # while A !=B:
        #     A = A.next if A else headB
        #     B = B.next if B else headA
        # return A

        # 求长度
        lenA, lenB = 0, 0
        cur = headA
        while cur:         # 求链表A的长度
            cur = cur.next 
            lenA += 1
        cur = headB 
        while cur:         # 求链表B的长度
            cur = cur.next 
            lenB += 1
        curA, curB = headA, headB

        