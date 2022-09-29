#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    
    def reverseList(self, head):
        prev=None
        curr=head
        next=None
        while(curr!=None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev
        
    #Function to add two numbers represented by linked list.
    
    def addTwoLists(self, first, second):
        head1=self.reverseList(first)
        head2=self.reverseList(second)
        
        anshead=Node(0)
        temp=anshead
        
        carry=0
        s=0
        
        while ((head1!=None or head2!=None) or carry>0):
            s=0
            if head1!=None:
                s+=head1.data
                head1=head1.next
            if head2!=None:
                s+=head2.data
                head2=head2.next
                
            s+=carry
            carry=s//10
            
            x=Node(s%10)
            temp.next=x
            temp=temp.next
            
        ans=self.reverseList(anshead.next)
        return ans
        
        # s1=""
        # s2=""
        # temp1=first
        # temp2=second
        # while temp1 is not None:
        #     s1+=str(temp1.data)
        #     temp1=temp1.next
        # while temp2 is not None:
        #     s2+=str(temp2.data)
        #     temp2=temp2.next
        # s1=int(s1)
        # s2=int(s2)
        # ans=s1+s2
        # ans=str(ans)
        # prevhead=None
        # head=None
        # f=0
        # for i in ans:
        #   if f==0:
        #       x=Node(int(i))
        #       head=x
        #       prevhead=x
        #       f=1
        #   else:
        #       x=Node(int(i))
        #       prevhead.next=x
        #       prevhead=x
        # return head

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends


'''

Example 1:

Input:
N = 2
valueN[] = {4,5}
M = 3
valueM[] = {3,4,5}
Output: 3 9 0  
Explanation: For the given two linked
list (4 5) and (3 4 5), after adding
the two linked list resultant linked
list will be (3 9 0).
Example 2:

Input:
N = 2
valueN[] = {6,3}
M = 1
valueM[] = {7}
Output: 7 0
Explanation: For the given two linked
list (6 3) and (7), after adding the
two linked list resultant linked list
will be (7 0).

'''
