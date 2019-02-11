# Fennell, Matthew
# CPTR 454
# HW 5 Programming Problem

# 6.3.10
# Write a program for constructing a 2-3 tree for a given list of n integers

# Basic 2-3 Tree Algorithm

# From the text: A 2-3 tree is a tree that can have 2-nodes or 3-nodes.

# 2-nodes: A 2-node contains a single key K and has two children:
# the left child serves as the root of a subtree whose keys are less than K, and
# the right child serves as the root of a subtree whose keys are greater than K.
# In other words, a 2-node is the same kind of node we have in the classical
# binary search tree.

# 3-nodes: A 3-node contains two keys K1 and K2 (K1<K2) and has three children.
# The leftmost child serves as the root of a subtree with keys less than K1.
# The middle child serves as the root of a subtree with keys between K1 and K2.
# The rightmost child serves as the root of a subtree with keys greater than K2.

# The last requirement of the 2-3 tree is that all its leaves must be on the same level.
# In other words, a 2-3 tree is always perfectly height balanced: the length of
# a path from the root to a leaf is the same for every leaf.

# On empty tree:
# Just make a node

# Otherwise:
# Search for K
# If you end on a 2 node: add as the first or second key
# If you end on a 3 node: split the leaf in two; put the smaller in one leaf, promote the middle, and put the largest in the other

import sys
import random
import math

if(len(sys.argv)==2):
    n_list_length = int(sys.argv[1])
else:
    print("Please input the number of integers to be generated: ")
    n_list_length = int(input())

print(n_list_length, "integers will be generated.")

n_list = []

for integer in range(n_list_length):
    integer = random.randint(1,50)
    n_list.append(integer)

for entry in n_list:
    print(entry)
