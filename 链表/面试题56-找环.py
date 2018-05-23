# -*- coding: utf-8 -*-
"""
Created on Wed May 23 15:02:12 2018

@author: sky
"""

'''
⼀一个链表中包含环，请找出该链表的环的⼊入⼝口结点。
思路：设置一个快指针，一次走两步，一个慢指针，一次走一步，
    第一次循环，当两指针相遇，说明有环。
    第二次循环，让快指针回到起点，当两指针再次相遇，则是换的起点，因为快指针比慢指针多走了一个环
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def EntryNodeOfLoop(self, pHead):
        if pHead == None:
            return 1
        if pHead.next == None or pHead.next.next == None:
            return None
        p = pHead.next.next
        q = pHead.next
        while p!=q:
            p = p.next.next
            q = q.next
            if p.next == None or p.next.next == None:
                return None
        p = pHead
        while p!=q:
            p = p.next
            q = q.next
        return q