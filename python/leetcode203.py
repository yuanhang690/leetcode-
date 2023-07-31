# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 可能会有删除头结点的情况
        # 添加一个虚拟头节点，对头节点的删除操作与其他节点一样
        pre_node = ListNode(next=head)
        node = pre_node
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        return pre_node.next
