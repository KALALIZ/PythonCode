#!/usr/bin/python


class Node:

    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class BST:

    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = val
        if val < self.root:
            self.root.l, val
        else:
            self.root.r, val

    def find(self, val):  # ให
        currNode = self.root
        while currNode:
            if currNode.get_data() == val:
                return currNode
            else:
                currNode = currNode.get_next()
            return None





        ########################## DO NOT EDIT ################
    def printTree(self):
        if(self.root is not None):
            self._printTree(self.root)
        print()

    def _printTree(self, node):
        if(node is not None):
            self._printTree(node.l)
            print(str(node.v), end=" ")
            self._printTree(node.r)


def main():

    tree = BST()
    tree.add(4)
    tree.add(6)
    tree.add(2)
    tree.add(20)
    tree.add(1)
    tree.add(3)
    tree.add(18)
    tree.printTree()
    print(tree.find(3))
    print(tree.find(32))

if __name__ == '__main__':
    main()