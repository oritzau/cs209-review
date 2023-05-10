
class Node:
    # instance variables
    # data - hold the data in the Node
    # next - reference the next Node (in a linked list)

    def __init__(self, d):
        self.data = d
        self.next = None

class LinkedList:

    # instance variable
    # __head - reference the first Node in the linked list

    def __init__(self):
        self.__head = None

    # O(1)
    def add_to_beginning(self, d): 
        new_node = Node(d)
        new_node.next = self.__head
        self.__head = new_node

    # O(n) without tail, O(1) with it
    def append(self, d):

        new_node = Node(d)
        if self.is_empty():
            self.__head = new_node
        else:    
            temp_node = self.__head
        
            # need to alter this condition so we do not go too far
            while temp_node.next != None:
                temp_node = temp_node.next
            
            # what is the value of temp_node here?
            # temp_node is last node now
        
            temp_node.next = new_node
        

    def is_empty(self):
        return self.__head == None
        #if self.__head == None:
        #    return True
        #else:
        #    return False

    def clear(self):
        self.__head = None  # this makes the list empty

    # O(n)
    def insert_after(self, lookfor, insert):
        # if lookfor doesn't exist
        # empty list a special case?  will empty list work here
        # if lookfor exists 
        temp_node = self.__head

        while temp_node != None and temp_node.data != lookfor:
            temp_node = temp_node.next

        # if we found lookfor
        # if temp_node.data == lookfor: # would crash if temp_node == None
        if temp_node != None:
            # when we get here, temp_node's data contains lookfor
            insert_node = Node(insert)
            insert_node.next = temp_node.next # this must be done 1st
            temp_node.next = insert_node # this 2nd

    # O(n)
    def remove(self, target):

        if not self.is_empty():

            if self.__head.data == target:
                self.__head = self.__head.next
            else:
                temp_node = self.__head

                while temp_node.next != None and temp_node.next.data != target:
                    temp_node = temp_node.next

                # temp_node is now the one before the node to remove (data is the target)
                # if temp_node.next.data == target:  can't do this because crash if temp_node.next == None
                if temp_node.next != None:
                    temp_node.next = temp_node.next.next
        

    def __str__(self):
        if self.is_empty():
            return ''
        else:
            string_to_return = ''
            temp_node = self.__head
            while temp_node.next != None:
                string_to_return += str(temp_node.data) + '\n'
                temp_node = temp_node.next
            string_to_return += str(temp_node.data)
            return string_to_return

    

        
