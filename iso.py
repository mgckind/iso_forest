"isolated forest functions"
__author__ = 'Matias Carrasco Kind'
import numpy as np
import random as rn
import os

class Node(object):
    def __init__(self, X, q, p, e, left, right, node_type = '' ):
        self.e = e
        self.size = len(X)
        self.X = X # to be removed
        self.q = q
        self.p = p
        self.left = left
        self.right = right
        self.ntype = node_type


class iTree(object):

    """
    Unique entries for X
    """

    def __init__(self,X,e,l):
        self.e = e # depth
        self.X = X
        self.size = len(X) #  n objects
        self.Q = np.arange(np.shape(X)[1], dtype='int') # n dimensions
        self.l = l # depth limit
        self.p = None
        self.q = None
        self.root = self.make_tree(X,e,l)
        

    def make_tree(self,X,e,l):
        self.e = e
        if e >= l or len(X) <= 1:
            left = None
            right = None
            return Node(X, self.q, self.p, e, left, right, node_type = 'exNode' )
        else:
            self.q = rn.choice(self.Q)
            self.p = rn.uniform(X[:,self.q].min(),X[:,self.q].max())
            w = np.where(X[:,self.q] < self.p,True,False)
            return Node(X, self.q, self.p, e,\
            left=self.make_tree(X[w],e+1,l),\
            right=self.make_tree(X[~w],e+1,l),\
            node_type = 'inNode' )
        
            


