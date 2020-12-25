#!/usr/bin/env python3
# ศิลาลักษณ์ แก้วจันทร์เพชร
# 610510670
# Lab 08
# Problem 1
# 204113 Sec 001

def add_code(node, label, result, prefix = ''):    

    child_node = node[label]     
    tree_huffman = {}
    
    if len(childs) == 2:
        tree_huffman['1'] = add_code(node, child_node[1], result, prefix+'1')
        tree_huffman['0'] = add_code(node, child_node[0], result, prefix+'0')     
        return tree
    else:
        result[label] = prefix
        return label

def huffman(value):


def main():
    ex1 = {'a': 35, 'b': 26, 'c': 12, 'd': 16, 'e': 17, 'f': 20}
    print(huffman(ex1))


if __name__ == '__main__':
    main()