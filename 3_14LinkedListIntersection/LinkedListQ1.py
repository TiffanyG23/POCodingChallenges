class ListElem:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Solution(object):
    def getIntersectionElem(self, headA, headB):
        """
        :type head1, head1: ListElem
        :rtype: ListElem
        """
        dict = {}
        while headA:
            dict[headA] = 1
            headA = headA.next
        while headB:
            if headB in dict:
                return headB
            headB = headB.next
        return None

headA = ListElem(4)
headB = ListElem(5)
Intersect = ListElem(8, ListElem(4, ListElem(5)))
headA.next = ListElem(1, Intersect)
headB.next = ListElem(0, ListElem(1, Intersect))
ob1 = Solution()
op = ob1.getIntersectionElem(headA, headB)
print("Intersection: ", op.data)