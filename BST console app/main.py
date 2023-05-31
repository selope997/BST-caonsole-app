import math
import binary_tree

def reArrange(arr):
    reArrangeArr = []  # array that will be returned
    arr.sort()
    print(arr)

    def callBack(arr):
        mid = math.floor(len(arr) / 2)

        if mid < 0:
            # add arr[mid] to reArrangeArr
            reArrangeArr.append(arr[mid])
            return
        
        elif len(arr) == 0:
            return
        
        else:
            reArrangeArr.append(arr[mid])

            right = arr[mid + 1:]
            left = arr[:mid]

            callBack(right)
            callBack(left)

    callBack(arr)
    print(reArrangeArr)

    return reArrangeArr


#======================================================================
while True:

    while True: 
        print("1. pre-load a sequense of integers to build a BST \n2. manually enter interger values, one by one, to build a BST \n3. exit")
        choice = input()
        
        if choice in ['1','2','3']:
            break
        else:
            print("invalid input, please enter 1, 2 or 3")

    tree = binary_tree.BinaryTree()

    # level 1

    if choice == "1":
        # 1
        sample = [58,84,68,23,38,82,26,17,24,106,95,48,88,54,50,51,53,49,-6,-46]
        
        for e in sample:
            tree.insert(e)

        binary_tree.printTree(tree.getRoot())

    elif choice == "2":
        # 2
        sample = []
        print("Please enter integers one by one and enter '-' after you enter the last elment\n")
        while True:
            try:
                e = input("enter new element : ")
                if e == "-":
                    break

                e = int(e)
                tree.insert(e)

            except:
                print("Error: please enter only integers or '-'")

        binary_tree.printTree(tree.getRoot())
        
    elif choice == "3":
        #3
        exit()

    # level 2

    while True:

        while True: 
            print("\n\n1. Display the tree shape of current BST, and then show the pre-order, in-order, post-order, and inverse-in-order traversal sequences of the BST")
            print("2. Show all leaf nodes of the BST and all non-leaf nodes (separately)")
            print("3. Show a sub-tree an count its nodes")
            print("4. Show the depth of a given node in the BTS")
            print("5. Show the depth of a subtree of the BST")
            print("6. Insert a new integer key into the BST")
            print("7. Delete and integer key from the BST")
            print("8. Exit")
            choice = input()
            
            if choice in ['1','2','3','4','5','6','7','8']:
                break
            else:
                print("invalid input, please enter a integer from 1 to 8")

        if choice == '1':
            # diplay tree shape
            binary_tree.printTree(tree.getRoot())
            print("\n Pre-order: ")
            tree.preorder()
            print("\n\n In-order: ")
            tree.inorder()
            print("\n\n Post-order: ")
            tree.postorder()
            print("\n\n Inverse-in-order: ")
            tree.inverse_inorder()

        elif choice == '2':
            print("\n Leaf nodes")
            tree.leaf_BST()
            print("\n non-leaf nodes")
            tree.non_leaf_BST()
        
        elif choice == '3':

            # ask user to enter an integer 
            while True:
                try:
                    N = int(input("\nEnter a node of the BST : "))
                    if N is not None:
                        break
                except:
                    print("\nInvalid input please enter and integer.")

            binary_tree.printTree(tree.find_node(N))

            # if the node is in the tree find_node returns the node otherwise dose not return anything 
            node = tree.find_node(N) 

            if node == None:
                print("\nError: Node "+ str(N) +" not found!")

            else:
                print("\nNodes rooted to "+ str(N) + " : ")
                count = tree.total_nodesBST(node)
                print("\n\nTotal number of nodes :")
                print(count)
        
        elif choice == '4':
            while True:
                try:
                    N = int(input("\nEnter a node of the BST : "))
                    if N is not None:
                        break
                except:
                    print("\nInvalid input please enter and integer.")

                                    
            node = tree.find_node(N) # if the node is in the tree 'find_node()' returns the node otherwise dose not return anything  

            if node is None:
                print("\nError: Node "+ str(N) +" not found!")

            else:
                tree.depth_nodeBST(N)
                
        elif choice == '5':
            while True:
                try:
                    N = int(input("\nEnter a node of the BST : "))
                    if N is not None:
                        break
                except:
                    print("\nInvalid input please enter and integer.")

                                    
            node = tree.find_node(N) # if the node is in the tree 'find_node()' returns the node otherwise dose not return anything  

            # if node was not found
            if node is None:
                print("\nError: subtree rooted at node "+ str(N) +" not found!")
            else:
                binary_tree.printTree(node)
                depth = tree.depth_subtreeBST(node)
                print("\nThe depth of "+ str(N) +" is : " + str(depth))
            
        elif choice == '6':

            while True:
                try:
                    N = int(input("\nEnter a node of the BST : "))
                    if N is not None:
                        break
                except:
                    print("\nInvalid input please enter and integer.")

            node = tree.find_node(N) # if the node is in the tree 'find_node()' returns the node otherwise dose not return anything  

            if node is None:
                tree.insert(N)
                tree.inverse_inorder()
            else:
                print("ERROR: node key "+str(N)+" already exist in the BST!")

        elif choice == '7':

            while True:
                try:
                    N = int(input("\nEnter a node of the BST : "))
                    if N is not None:
                        break
                except:
                    print("\nInvalid input please enter and integer.")

            node = tree.find_node(N) # if the node is in the tree 'find_node()' returns the node otherwise dose not return anything  
            
            if node is None:
                print("\nError: Node "+ str(N) +" not found!")
                
            else: # if node was found delete the node an print the inverse-in-order traversal sequense 
                tree.delete(N)
                tree.inverse_inorder()

        elif choice == '8' :
            break

