# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 18:34:01 2023

@author: Johann-Friedrich Salzmann, Finn Krüger
"""

class Empty(Exception): pass


class ArrayDequeMaxlen():
    
    def __init__(self,max):
        # This implementation is done with python lists, so no need to have a front pointer
        # and the order of the list will consistently indicate the order of the queue
        self._data = []
        self.__max = max
        
    def __len__(self): # length of AQM should be length of the list
        return len(self._data)
    
    def __getitem__(self, index): # direct AQM element access
        return self._data[index]
    
    def __repr__(self): # string representation of AQM
        return str(self._data)
    
    @property
    def _front(self):
        # This implementation is done with python lists, so no need to have a front pointer
        # and the order of the list will consistently indicate the order of the queue
        # -> This is only added for interface compatibility reasons
        return 0
        
    def add_first(self,e): # add element in front of the queue and delete at the end if max length reached
        if(self.__len__() == self.__max):
            self.delete_last()
        self._data.insert(0,e)
        
    def add_last(self,e): # add element at the end of the queue and delete in front if max length reached
        if(self.__len__() == self.__max):
            self.delete_first()
        self._data.append(e)
        
    def delete_first(self): # delete element in front
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data.pop(0)
        
    def delete_last(self): # delete element at the end
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data.pop()
        
    def remove(self,e): # remove all elements of a given value from the queue
        if self.is_empty():
            raise Empty('Queue is empty')
        while e in self._data:
            self._data.remove(e)
        
    def first(self): # return first element
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[0]
        
    def last(self): # return last element
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[-1]
        
    def is_empty(self): # return whether queue is empty
        return len(self._data) == 0
        
    
                
        
        
   