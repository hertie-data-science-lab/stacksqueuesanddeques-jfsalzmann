# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 18:34:20 2023

@author: Johann-Friedrich Salzman, Finn Krüger
"""

from ArrayDeque import ArrayDequeMaxlen

# PLEASE NOTE
# We noticed that the commands given in the main.py initially
# did not at all match the interface definition of the AQM class
# as provided at Github. Additionally, some methods used here were
# not defined in the task on Github. We handled the situation as
# follows: We followed the names and basic instructions on Github,
# and added the missing methods according to the main.py.
# As stated in the class, we relied on not having to implement
# the AQM with Arrays, so we have a dynamic length list underlying
# with no need to have length adjustment, or use a front pointer.
     
        
AQM = ArrayDequeMaxlen(20)


print('Adding last')
for i in range(100):
    AQM.add_last(i)
    print (i, AQM)
    
print('\nDelete 80', AQM.remove(80), AQM, AQM._front)
    


    
print ('\nAdding first')
for i in range(20, 10, -1):
    AQM.add_first(i)
    print (i, AQM)
    
    
print(AQM._front)
    

    
print('\nPerforming the removals')
while not AQM.is_empty():
    print ('Remove first', AQM.first(), AQM.delete_first(), 'Remove last', AQM.last(),  AQM.delete_last())