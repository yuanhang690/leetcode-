class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 暴力解法
        # # 虚拟头结点，可能会有删除第一个结点的情况
        # dummyhead = ListNode(0,head)
        # cur = dummyhead
        # sz = 0
        # while head.next:
        #     head = head.next
        #     sz += 1

        # for i in range(sz-n+1):
        #     cur = cur.next
        # cur.next = cur.next.next
        # return dummyhead.next
        #

        # 解法2：栈

        # stack = []
        # dummyhead = ListNode(0,head)
        # cur = dummyhead
        # while cur:
        #     stack.append(cur)
        #     cur = cur.next
        # for i in range(n):
        #     stack.pop()
        # cur = stack[-1]
        # cur.next = cur.next.next
        
        # return dummyhead.next

        #解法三：双指针
        # 
