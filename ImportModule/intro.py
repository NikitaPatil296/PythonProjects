#import my_module
#import my_module as mod
#from my_module import find_index , test
'''Hard to track where the function or variable came from '''
from my_module import * 

'''How to find module location:
1. script location
2. python path environment variable
3. standard library directory
4. site packages directory for third party packages'''
import sys


cources = ['History','math','physics','compSci']

# index = my_module.find_index(cources,'physics')
# index = mod.find_index(cources,'physics')
index = find_index(cources,'physics')
#print(index)
#print(test)
print(sys.path)