# -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:09:15 2018

@author: sky
"""

'''
面试题16 ：输入一个链表，反转链表后，输出链表的所有元素。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def ReverseList(self,pHead):
        if not pHead:
            return None
        Pre = None
        Next = None
        while pHead:
            Next = pHead.next
            pHead.next = Pre
            Pre = pHead
            pHead = Next
        return Pre