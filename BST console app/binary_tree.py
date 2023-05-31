from ast import And


def printTree(root, element="element", left="left", right="right"):                                 ##  https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    def display(root, element=element, left=left, right=right):                                     ##  AUTHOR: Original: J.V.     Edit: BcK
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, element)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, element)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, element)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, element)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    
    lines = []
    if root != None:
        lines, *_ = display(root, element, left, right)
    print("\t== Binary Tree: shape ==")
    print()
    if lines == []:
        print("\t  No tree found")
    for line in lines:
        print("\t", line)
    print()

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    # Return True if the element is in the tree
    def depth_nodeBST(self, e):
        current = self.root # Start from the root
        depth = 0
        while current != None:
            if e < current.element:
                current = current.left
                depth += 1
            elif e > current.element:
                current = current.right
                depth += 1
            else: # element matches current.element
                print("this is the depth of "+ str(e) + " : " + str(depth))
                return True # Element is found
            

        return False
    
    # Return True if the element is in the tree
    def search(self, e):
        current = self.root # Start from the root
        
        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else: # element matches current.element
                return True # Element is found
            
        return False
    
    def find_node(self, e):
        current = self.root # Start from the root

        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else: # element matches current.element
                return current # Element is found

        

    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully
    def insert(self, e):
        if self.root == None:
          self.root = self.createNewNode(e) # Create a new root
        else:
          # Locate the parent node
          parent = None
          current = self.root
          while current != None:
            if e < current.element: #
              parent = current
              current = current.left
            elif e > current.element:
              parent = current
              current = current.right
            else:
              return False # Duplicate node? not inserted

          # Create the new node and attach it to the parent node
          if e < parent.element:
            parent.left = self.createNewNode(e)
          else:
            parent.right = self.createNewNode(e) 
        self.size += 1 # Increase tree size
        return True # Element inserted

    # Create a new TreeNode for element e
    def createNewNode(self, e):
      return TreeNode(e)
    """
    # Return the size of the tree
    def getSize(self):
      return self.size"""

    # 
    def non_leaf_BST(self):
      self.non_leaf_BST_Helper(self.root)

    # 
    def non_leaf_BST_Helper(self, r):
      if r != None:
        self.non_leaf_BST_Helper(r.left)
        if r.left != None or r.right != None:
            print(r.element, end = " ")
        self.non_leaf_BST_Helper(r.right)

    # 
    def leaf_BST(self):
      self.leaf_BST_Helper(self.root)

    # 
    def leaf_BST_Helper(self, r):
      if r != None:
        self.leaf_BST_Helper(r.left)
        # if dosen't have children 
        if r.left == None and r.right == None:
            print(r.element, end = " ")
        self.leaf_BST_Helper(r.right)

    # Inorder traversal from the root
    def inorder(self):
      self.inorderHelper(self.root)

    # Inorder traversal from a subtree
    def inorderHelper(self, r):
      if r != None:
        self.inorderHelper(r.left)
        print(r.element, end = " ")
        self.inorderHelper(r.right)
    
    # inverse Inorder traversal from the root
    def inverse_inorder(self):
      self.inverse_inorderHelper(self.root)

    # inverse Inorder traversal from a subtree
    def inverse_inorderHelper(self, r):
      if r != None:
        self.inverse_inorderHelper(r.right)
        print(r.element, end = " ")
        self.inverse_inorderHelper(r.left)

    # Postorder traversal from the root
    def depth_subtreeBST(self, N):
      if N is None:
         return 0
      else:
         left_depth = self.depth_subtreeBST(N.left)
         right_depth = self.depth_subtreeBST(N.right)
         max_depth = max(left_depth, right_depth)

         return max_depth + 1
      
    # Preorder traversal from the root
    def preorder(self):
      self.preorderHelper(self.root)

    # Preorder traversal from a subtree
    def preorderHelper(self, root):
      if root != None:
        print(root.element, end = " ")
        self.preorderHelper(root.left)
        self.preorderHelper(root.right)
    
    # Postorder traversal from the root
    def postorder(self):
      self.postorderHelper(self.root)

    # Postorder traversal from a subtree
    def postorderHelper(self, root):
      if root != None:
        self.postorderHelper(root.left)
        self.postorderHelper(root.right)
        print(root.element, end = " ")


    def total_nodesBST(self, N): 
        if N is None:
            return 0
        else:
            count = 1
            print(N.element, end=' ')
            count += self.total_nodesBST(N.left)
            count += self.total_nodesBST(N.right)
            return count

    
    # Return true if the tree is empty
    def isEmpty(self):
      return self.size == 0

    # Remove all elements from the tree
    def clear(self):
      self.root == None
      self.size == 0

    # Return the root of the tree
    def getRoot(self):
      return self.root
    
    def delete(self, elem):
        parent = None
        curr = self.root

        while curr is not None: # find the node 
            if elem == curr.element:
                # Case 1: Node to be deleted is a leaf node
                if curr.left is None and curr.right is None:
                    if parent is None:
                        self.root = None
                    elif parent.left == curr:
                        parent.left = None
                    else:
                        parent.right = None

                # Case 2: Node to be deleted has only one child
                elif curr.left is None:
                    if parent is None:
                        self.root = curr.right
                    elif parent.left == curr:
                        parent.left = curr.right
                    else:
                        parent.right = curr.right

                elif curr.right is None:
                    if parent is None:
                        self.root = curr.left
                    elif parent.left == curr:
                        parent.left = curr.left
                    else:
                        parent.right = curr.left

                # Case 3: Node to be deleted has two children
                else:
                    successor_parent = curr
                    successor = curr.right
                    while successor.left is not None:
                        successor_parent = successor
                        successor = successor.left

                    curr.element = successor.element

                    if successor_parent.left == successor:
                        successor_parent.left = successor.right # successor will be none
                    else:
                        successor_parent.right = successor.right

                return

            elif elem < curr.element:
                parent = curr
                curr = curr.left
            else:
                parent = curr
                curr = curr.right

class TreeNode:
    def __init__(self, e):
      self.element = e
      self.left = None # Point to the left node, default None
      self.right = None # Point to the right node, default None