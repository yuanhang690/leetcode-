from pyparsing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         # 为啥错？
#         # if not head.next:
#         #     return None
#         # dummyhead = ListNode(0)
#         # dummyhead.next = head
#         # while dummyhead:
#         #     cur = dummyhead.next
#         #     while cur:
#         #         if cur.next == dummyhead:
#         #             return dummyhead
#         #         cur = cur.next
#         #     dummyhead = dummyhead.next

#         # return None
#         # unorder_set = set()
#         # while head!=None:
#         #     if head in unorder_set:
#         #         return head
#         #     unorder_set.add(head)
#         #     head = head.next

#         #　解法二：快慢指针（待完善）

#  快慢指针
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 设置快慢指针
        slow = head
        fast = head
        while fast and fast.next:
            # 每次走一步
            slow = slow.next
            # 每次走两步
            fast = fast.next.next


            # 相遇
            if slow == fast:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        # 直接到尾也没成环就返回
        return None





# p1 = ListNode(3)
# p2 = ListNode(2)
# p3 = ListNode(0)
# p4 = ListNode(-4)
# p1.next = p2
# p2.next = p3
# p3.next = p4
# p4.next = p2

# solution = Solution()
# res:ListNode = solution.detectCycle(p1)

# print(res.val)