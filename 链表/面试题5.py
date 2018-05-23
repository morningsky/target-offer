# -*- coding: utf-8 -*-
"""
Created on Wed May 23 11:49:40 2018

@author: sky
"""

'''
    面试题5： 从尾到头打印链表
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution1:
    def printList(self, listNode):
        L = []
        #直接遍历一边列表保存结果到list中再返回倒序的list
        while listNode:
            L.append(listNode.val)
            listNode = listNode.next
        return L[::-1]
    
from collections import deque
class Solution2:
    def printList2(self, listNode):
        if listNode is None:
            return []
        queue = deque()
        while listNode:
            queue.appendleft(listNode.val) ## 将当前的listNode结点的value放到队列列的最左侧，即可反 向输出链表
            listNode = listNode.next
        return queue
    