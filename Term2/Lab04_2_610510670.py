#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 04
# Problem 2
# 204113 Sec 001


class Node(object):
    # constructor

    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d

########################################################################


class LinkedList(object):

    def __init__(self, r = None):
        self.root = r

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node

    def insert_in_order(self, d):
        if self.root == None or self.root.get_data() > d:
            self.add(d)  # add to root Node
        else:
            currNode = self.root  # Define currNode
            while currNode.get_next() and currNode.get_next().get_data() < d:
                currNode = currNode.get_next()
            newNode = Node(d, None)
            newNode.set_next(currNode.get_next())
            currNode.set_next(newNode)
            return newNode

    def remove(self, d):
        currNode = self.root
        prev_node = None
        while currNode:
            if currNode.get_data() == d:
                if prev_node:
                    prev_node.set_next(currNode.get_next())
                else:
                    self.root = currNode.get_next()
                return True
            else:
                prev_node = currNode
                currNode = currNode.get_next()
        return False

    def print(self):
        root_node = self.root
        if root_node == None:
            print()
            return
        print(root_node.data, end=' ')
        while root_node.next_node != None:
            print(root_node.get_next().data, end=' ')
            root_node = root_node.get_next()
        print()

#############################################################


def main():
    List = LinkedList()
    info = int(input())
    for i in range(info):
        ans = input().split(" ")
        if ans[0] == 'i':
            List.insert_in_order(int(ans[1]))
        elif ans[0] == 'd':
            i = int(ans[1])
            result = List.remove(i)
            if result:
                print(i, "[removed]")
            else:
                print(i, "[not removed]")
        elif ans[0] == 'p':
            List.print()

if __name__ == '__main__':
    main()
