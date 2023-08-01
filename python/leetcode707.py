class ListNode:
    def __init__(self,val = 0,next = None) -> None:
        self.val = val
        self.next = next


class MyLinkedList:

# 使用虚拟头结点，一个变量记录总长度

    def __init__(self):
        self._dummyHead = ListNode()
        self._size = 0

    def get(self, index: int) -> int:
        if index >=self._size:
            return -1
        


        cur = self._dummyHead.next
        for i in range(index):
            cur = cur.next

        return cur.val


    def addAtHead(self, val: int) -> None:
        newnode = ListNode(val=val)
        newnode.next = self._dummyHead.next
        self._dummyHead.next = newnode
        self._size +=1



    def addAtTail(self, val: int) -> None:
        cur = self._dummyHead
        while cur.next != None:
            cur = cur.next
        
        newnode = ListNode(val=val)
        cur.next = newnode
        self._size +=1



    def addAtIndex(self, index: int, val: int) -> None:
        if index >self._size:
            return
        cur = self._dummyHead
        while index:
            cur = cur.next
            index -= 1
        newnode = ListNode(val=val)
        newnode.next = cur.next
        cur.next = newnode
        self._size +=1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self._size:
            return
        cur = self._dummyHead
        while index :
            cur = cur.next
            index -= 1

        cur.next = cur.next.next
        self._size -= 1