from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        target = deque()
        pointer = head
        answer = True
        
        while pointer != None:
            target.append(pointer.val)
            pointer = pointer.next
            
        while len(target) > 1:
            a,b = target.popleft(), target.pop()
            
            if a != b:
                answer = False
                
        return answer
            
            