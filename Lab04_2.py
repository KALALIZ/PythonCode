class Node(object):
    def __init__(self, d, n=None):
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

#------------------end of class Node -------------------#

class LinkedList(object):

    def __init__(self, r=None):
        self.root = r

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node

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
        x = self.root
        if x == None:
            print()
            return
        print(x.data,end=' ')
        while x.next_node != None:
            print(x.get_next().data,end=' ')
            x = x.get_next()
        print()

    def insert_in_order(self, d):
        if self.root == None or self.root.get_data() > d:
            self.add(d)
        else:
            currNode = self.root # Define currNode
            while currNode.get_next() and currNode.get_next().get_data() < d:
                    currNode = currNode.get_next()
            newNode = Node(d, None)
            newNode.set_next(currNode.get_next())
            currNode.set_next(newNode)
            return newNode
            
#------------------end of class LinkedList -------------------#


def main():  
    myList = LinkedList()
    total = int(input())
    for i in range(total):
        order = input().split(" ")

        if order[0] == 'i':
            myList.insert_in_order(int(order[1]))
        elif order[0] == 'd':
            i = int(order[1])
            result = myList.remove(i)
            if result:
                print(i, "[removed]")
            else:
                print(i, "[not removed]")
        elif order[0] == 'p':
            myList.print()


if __name__ == '__main__':
    main()
