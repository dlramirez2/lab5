#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 10:37:24 2018

@author: Diana Ramirez 88604827
CS3 Lab 4B
Professor D. Aguirre
TA Nath
1:30PM 
"""
class Heap:
    def __init__(self):
        self.heap_array =[]
        
    def insert (self,k):
        self.heap_array.append(k)
        self.percolate_up(len(self.heap_array) - 1)
        
    def extract_min(self):
        if self.is_empty():
            return None
        min_elem = self.heap_array[0]
        ##placing the last value of the heap in index[0]
        new_val = self.heap_array.pop()
        
        if len(self.heap_array)>0:
            self.heap_array[0] = new_val
            self.percolate_down(0)
        return min_elem
    
    def is_empty(self):
        return len(self.heap_array)==0
    
        
    ##To keep the Min heap properties I used the following methods
    ##used percolate_up to insert a new number in the heap
    def percolate_up(self, node_index):
        while node_index > 0:
        # compute the parent node's index
            parent_index = (node_index - 1) // 2
       
            if self.heap_array[node_index] >= self.heap_array[parent_index]:
            # no violation, so percolate up is done.
                return
            else:
            # swap heap_array[node_index] and heap_array[parent_index]
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[parent_index]
                self.heap_array[parent_index] = temp
            
            # continue the loop from the parent node
                node_index = parent_index 
                
    ##used percolate_down to extract_min from the heap
    def percolate_down(self, node_index):
        child_index = 2 * node_index + 1
        value = self.heap_array[node_index]

        while child_index < len(self.heap_array):
            # Find the min among the node and all the node's children
            min_value = value
            min_index = -1
            i = 0
            while i < 2 and i + child_index < len(self.heap_array):
                if self.heap_array[i + child_index] < min_value:
                    min_value = self.heap_array[i + child_index]
                    min_index = i + child_index
                i = i + 1

            # check for a violation of the min heap property
            if min_value == value:
                return
            else:
                # swap heap_array[node_index] and heap_array[min_index]
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[min_index]
                self.heap_array[min_index] = temp
                
                # continue loop from the min index node
                node_index = min_index
                child_index = 2 * node_index + 1
   
    ##heap sort implementation
    def heap_sort(self):
        heap_sorted = Heap()
        while len(self.heap_array)>0:
            min_dummy = self.extract_min()
            heap_sorted.insert(min_dummy)
        return heap_sorted
    

unsorted_heap = Heap()

g = open("numlist.txt")
num_list = g.readlines()


##populating the heap from the num list
for ln in num_list:
    ln = int(ln.replace('\n',''))
    unsorted_heap.insert(ln)
print(unsorted_heap.heap_array)

unsorted_heap = unsorted_heap.heap_sort()

print("Sorted heap: ")
print(unsorted_heap.heap_array)
 

