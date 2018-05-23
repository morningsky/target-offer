# -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:00:20 2018

@author: sky
"""
'''
    获取链表倒数第K个节点
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution1:
    '''
        先计算链表的长度，计算得找到倒数第K个需要几重循环
    '''
    def getReverseK(self,head,k):
        len_node = 0 
        temp = head 
        while temp: 
            temp = temp.next 
            len_node += 1
            
        run_times = len_node - k 
        if run_times < 0 or k < 0: 
            return
        for i in range(run_times): 
            head = head.next
        return head
    