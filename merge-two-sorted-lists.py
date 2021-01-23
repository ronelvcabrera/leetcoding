"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmpList = ListNode(0)
        mergeList = tmpList
        while (l1 != None and l2 != None):
            if l1.val < l2.val:
                tmpList.next = l1
                l1 = l1.next
            else:
                tmpList.next = l2
                l2 = l2.next
            tmpList = tmpList.next
        if l1 != None:
            tmpList.next = l1
        else:
            tmpList.next = l2
        return mergeList.next


def listContent(listNode):
    print('--- CHECKING ---')
    nextNode = listNode
    while (nextNode):
        print(nextNode.val)
        nextNode = nextNode.next
    print('-------')

l1 = ListNode(1, ListNode(3, ListNode(7)))
l2 = ListNode(2, ListNode(4, ListNode(6)))
sol = Solution()
answer = sol.mergeTwoLists(l1, l2)

# Checking answer
print("Checking Answer!!")
nextNode = answer
while (nextNode):
    print(nextNode.val)
    nextNode = nextNode.next
