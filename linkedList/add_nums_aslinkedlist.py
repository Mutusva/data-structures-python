# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:
  def addTwoNumbers(self, l1, l2, c=0):
        # Fill this in.
        num1 = ""
        num2 = ""
        cur = l1
        while cur:
            num1 = str(cur.val) + num1 
            cur = cur.next

        cur = l2
        while cur:
            num2 =  str(cur.val) + num2
            cur = cur.next

        sum = int(num1) + int(num2)
        result = str(sum)[::-1]

        root = None
        for i in range(0, result.__len__()):
           val = int(result[i])
           root = self.AddNodeRecursive(val, root)

        return root

  def AddToNodeIterative(self, val, node):
    if node is None:
      return ListNode(val)
    else:
         cur = node
         while cur.next:
             cur = cur.next
         cur.next = ListNode(val)
    return node

  def AddNodeRecursive(self, val, node):
    if node is None:
      return ListNode(val)
    else:
        if node.next is None:
            node.next = ListNode(val)
        else:
            self.AddNodeRecursive(val, node.next)
        return node
        
        

       
       
        

   
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)


while result:
  print(result.val)
  result = result.next
