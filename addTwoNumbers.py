#!usr/bin/env python3
#-*- coding:utf-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag = 0
        res = ListNode(0)
        tmp = res
        tmpsum = 0
        while l1 != None or l2 != None:
            if (l1 != None):
                tmpsum = tmpsum + l1.val
                l1 = l1.next
                
            if(l2 != None):
                tmpsum = tmpsum + l2.val
                l2 = l2.next
                
            tmpsum = tmpsum + flag
            tmp.next = ListNode(tmpsum % 10)
            tmp = tmp.next
            flag = tmpsum / 10
            
        if flag == 1:
            tmp.next = ListNode(1)
            
        return res.next
