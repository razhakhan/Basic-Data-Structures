'''
In this method, a temporary node is created. The next pointer of each node that is traversed is made to point to this temporary node. This way we are using the next pointer of a node as a flag to indicate whether the node has been traversed or not. Every node is checked to see if the next is pointing to a temporary node or not. In the case of the first node of the loop, the second time we traverse it this condition will be true, hence we return that node. 
The code runs in O(n) time complexity and uses constant memory space.

Below is the implementation of the above approach:
'''


# Python3 program to return first node of loop
class Node:
     
    def __init__(self, x):
         
        self.key = x
        self.next = None
 
# A utility function to print a linked list
def printList(head):
     
    while (head != None):
        print(head.key, end = " ")
        head = head.next
         
# Function to detect first node of loop
# in a linked list that may contain loop
def detectLoop(head):
     
    # Create a temporary node
    temp = Node(-1)
     
    while (head != None):
         
        # This condition is for the case
        # when there is no loop
        if (head.next == None):
            return None
 
        # Check if next is already
        # pointing to temp
        if (head.next == temp):
            break
 
        # Store the pointer to the next node
        # in order to get to it in the next step
        nex = head.next
 
        # Make next point to temp
        head.next = temp
 
        # Get to the next node in the list
        head = nex
 
    return head
 
# Driver code
if __name__ == '__main__':
     
    head = Node(50)
    head.next = Node(20)
    head.next.next = Node(15)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(10)
 
    # Create a loop for testing
    head.next.next.next.next.next = head.next.next
 
    res = detectLoop(head)
     
    if (res == None):
        print("Loop does not exist")
    else:
        print("Loop starting node is ", res.key)
 
# This code is contributed by mohit kumar 29
