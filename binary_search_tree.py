class BSTNode:
    # instance variables
    # data -- data stored in the node
    # left -- a reference to the current node's left BSTNode
    # right -- a reference to the current node's right BSTNode

    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    # instance variable(s):
    # __root is the root of the tree

    def __init__(self):
        self.__root = None

    def get_root_data(self):
        return self.__root.data
    
    # Theta(log(n)), but can take up to O(n) when inserted data was already mostly sorted
    def insert(self, d):
        node_to_insert = BSTNode(d)

        # is the tree empty
        if self.__root == None:    
            self.__root = node_to_insert
            #print(f'{d} inserted at the root')
        else:
            temp_node = self.__root
            while True:
                if d < temp_node.data:
                    if temp_node.left == None:
                        # insert it to the left of temp_node
                        temp_node.left = node_to_insert
                        #print(f'{d} inserted on left of {temp_node.data}')
                        break
                    else:
                        #print('going left')
                        temp_node = temp_node.left
                else:
                    if temp_node.right == None:
                        # insert it to the right of temp_node
                        temp_node.right = node_to_insert
                        #print(f'{d} inserted on right of {temp_node.data}')
                        break
                    else:
                        #print('going right')
                        temp_node = temp_node.right

            node_to_insert.parent = temp_node

    # recursive implementation of search
    def searchR(self, d):
        return self.searchR2(d, self.__root)

    # this is a recursive method that returns True if d is
    # found in the subtree starting at stroot
    
    def searchR2(self, d, stroot):
        # base case d was not found in the tree
        if stroot == None:
            return False

        # base case d was found
        if d == stroot.data:
            return True

        # recurse if d is not == stroot.data
        # but go left or right appropriately
        if d < stroot.data:
            return self.searchR2(d, stroot.left)
        else:
            return self.searchR2(d, stroot.right)
        
        
        
    def search(self, d):
        # should return True if d is found in the binary search tree
        # should return False otherwise
        temp_node = self.__root
        while temp_node != None and temp_node.data != d:
            if d < temp_node.data:
                # go left
                temp_node = temp_node.left
            else:
                temp_node = temp_node.right

        #if temp_node == None:
        #    return False
        #else:
        #    return True

        return temp_node
               
    def in_order(self):
        # print in_order of left
        # print root
        # print in_order of right
        if self.__root != None:
            self.__in_orderR(self.__root)

    def __in_orderR(self, subtree_root):
        if subtree_root.left != None:
            self.__in_orderR(subtree_root.left)

        print(str(subtree_root.data))

        if subtree_root.right != None:
            self.__in_orderR(subtree_root.right)

    def RMN_in_LST(self, root_above):
        temp = root_above.left
        while temp.right != None:
            temp = temp.right
        return temp

    def remove(self, d):
        node_to_remove = self.search(d)
        if node_to_remove == None:
            return False
        else:
            # check if leaf
            if node_to_remove.left == None and node_to_remove.right == None:
                if self.__root == node_to_remove:
                    # remove the root
                    self.__root = None
                else:
                    # we have to set node_to_remove's parent's correct child to None
                    if node_to_remove.parent.left == node_to_remove:
                        node_to_remove.parent.left = None
                    else:
                        node_to_remove.parent.right = None
            elif node_to_remove.left != None and node_to_remove.right != None:
                # the node_to_remove has two children
                # so we agreed to find RMN in LST of node_to_remove and replace
                # the value
                # then remove RMN in LST
                rmn_in_lst = self.RMN_in_LST(node_to_remove)

                node_to_remove.data = rmn_in_lst.data

                if rmn_in_lst.parent.right == rmn_in_lst:
                    # means he is his parent's right child
                    rmn_in_lst.parent.right = rmn_in_lst.left
                else:
                    # means he is his parent's left child
                    rmn_in_lst.parent.left = rmn_in_lst.left

                # parent needs to be set if a left child exists
                if rmn_in_lst.left != None:
                    rmn_in_lst.left.parent = rmn_in_lst.parent
            else:
                # node_to_remove has only 1 child
                if node_to_remove == node_to_remove.parent.left:
                    # node_to_remove is his parent's left child
                    
                    if node_to_remove.left == None:
                        # node_to_remove only has a right child
                        node_to_remove.right.parent = node_to_remove.parent
                        node_to_remove.parent.left = node_to_remove.right
                    else:
                        # node_to_remove only has a left child        
                        node_to_remove.left.parent = node_to_remove.parent
                        node_to_remove.parent.left = node_to_remove.left
                else:
                    # node_to_remove is his parent's right child
                    if node_to_remove.left == None:
                        node_to_remove.right.parent = node_to_remove.parent
                        node_to_remove.parent.right = node_to_remove.right
                    else:
                        node_to_remove.left.parent = node_to_remove.parent
                        node_to_remove.parent.right = node_to_remove.left

            return True
        
        
    
