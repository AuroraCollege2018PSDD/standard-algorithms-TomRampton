""" Short, one line description of the module ending with a period.
A longer description of the module with details that may help the user or anybody
reviewing the code later. make sure you outline in detail what the module does and how it can be used.
"""

__author__ = "Your Name"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "your.address@education.nsw.com.au"
__status__ = "Prototype, Development or Production"


""" revision notes:


"""
#include statements

from arrayloading import *
from arrayprinting import *
from sumarray import *
#other setup stuff
Array = []
numberArray = []

#now the real stuff we came here for
def main():
    loadArray(Array)
    numberArray = list(map(int, Array))
    printArray(numberArray)
    sumArray(numberArray)
       
if __name__ == '__main__':

   main()    
        


    
