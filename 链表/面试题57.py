# -*- coding: utf-8 -*-
"""
Created on Wed May 23 15:14:17 2018

@author: sky
"""
'''
    面试题57：
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def delDuplication(self,pHead):
        if not pHead:
            return None
        first = ListNode(0) #生成一个新的头指针
        last = first
        first.next = pHead
        tmp = pHead
        while tmp and tmp.next:
            if tmp.val == tmp.next.val:
                while tmp.next and tmp.val == tmp.next.val:
                    tmp = tmp.next
            else:
                last.next = tmp #删除链表中重复的结点
                last = last.next
            tmp = tmp.next
        return first.next
        
    