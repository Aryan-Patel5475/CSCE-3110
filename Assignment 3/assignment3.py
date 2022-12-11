import sys

class TreeNode():

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVL():

    def height(self, root):

        if not root:
            return 0

        return root.height

    def balance(self, root):

        if not root:
            return 0

        return self.height(root.left) - self.height(root.right)

    def MinimumVal(self, root):

        if root is None or root.left is None:
            return root

        return self.MinimumVal(root.left)

    def insert_node(self, root, key):

        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance_num = self.balance(root)

        if balance_num > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance_num < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def delete_node(self, root, key):

        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.MinimumVal(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance_num = self.balance(root)

        if balance_num > 1:
            if self.balance(root.left) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance_num < -1:
            if self.balance(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def right_rotate(self, num):

        num2 = num.left
        temp = num2.right
        num2.right = num
        num.left = temp

        num.height = 1 + max(self.height(num.left), self.height(num.right))
        num2.height = 1 + max(self.height(num2.left), self.height(num2.right))

        return num2

    def left_rotate(self, num):

        num2 = num.right
        temp = num2.left
        num2.left = num
        num.right = temp

        num.height = 1 + max(self.height(num.left), self.height(num.right))
        num2.height = 1 + max(self.height(num2.left), self.height(num2.right))

        return num2

    def print_tree(self, currPtr, indent, last):

        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("r ")
                indent += " | "
            else:
                sys.stdout.write("l ")
                indent += " | "
            print(currPtr.key)
            self.print_tree(currPtr.left, indent, False)
            self.print_tree(currPtr.right, indent, True)

tree = AVL()
root = None

root = tree.insert_node(root, 100)
root = tree.insert_node(root, 30)
root = tree.insert_node(root, 20)
root = tree.insert_node(root, 50)
tree.print_tree(root, "", True)
print()

root = tree.delete_node(root, 30)
tree.print_tree(root, "", True)
print()

root = tree.insert_node(root, 990)
root = tree.insert_node(root, 900)
tree.print_tree(root, "", True)
