"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]
"""
def listContent(listNode):
    print('--- CHECKING ---')
    nextNode = listNode
    while (nextNode):
        print(nextNode.val)
        nextNode = nextNode.next
    print('-------')

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        listed = []
        current = head
        prev = current
        while (current != None):
            if current.val not in listed:
                listed.append(current.val)
                prev = current
                current = current.next
            else:
                prev.next = current.next
                current = current.next
        return head


data = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(1, ListNode(1)))))))
solution = Solution()
listContent(solution.deleteDuplicates(data))