# -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:30:29 2018

@author: sky
"""

'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减 规则
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def Merge(self, pHead1, pHead2):  
        merged = None
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
    #第一个链表中的第一个点小于第二个链表的第一个点
    #则merged的第一个点就是pHead1的第一个点
    #对于他的next，继续递归 否则相反
        if pHead1.val < pHead2.val:
            merged = pHead1
            merged.next = self.Merge(pHead1.next, pHead2)
            
        else:
            merged = pHead2
            merged.next = self.Merge(pHead1, pHead2.next)
        return merged
