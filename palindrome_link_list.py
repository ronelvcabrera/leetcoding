class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    data = []
    node = head
    while node:
        data.append(node.val)
        node=node.next
    if len(data) == 0:
        return True
    index = 1 if len(data) % 2 == 1 else 0
    first_half = data[0:int(len(data)/2)]
    second_half = data[int(len(data)/2) + index:len(data)]
    first = ''.join([str(dat) for dat in first_half])
    second = ''.join([str(dat) for dat in second_half[::-1]])
    return first == second
data = ListNode(0, ListNode(0))
# data = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print(isPalindrome(data))