class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    node = head
    reversed = None
    while node:
        print(node.val)
        reversed = ListNode(node.val, reversed)
        node = node.next
    return reversed


def reverseListTrack(head):
    prev = None
    while head != None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev

def reseseListNode(head):
    reverseListRecursion(head)

def reverseListRecursion(head):
    if head.val == None or head.next == None:
        return head
    reverse = reverseListRecursion(head.next)
    head.next.next = head
    head.next = None
    reverse.next = head
    print(reverse.val)
    return reverse
data = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(reverseListTrack(data).val)
# print(reverseListRecursion(data))
# ListNode(3, ListNode(2, ListNode(1))
# reverseList(data)