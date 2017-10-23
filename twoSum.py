#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def twoSum(nums, target):
    dictionary = {}
    for i in range(0, len(nums)):
        if target - nums[i] in dictionary:
            return [ i, dictionary[target - nums[i]] ]

print( twoSum([2, 7, 11, 15], 9) )
