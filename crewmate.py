'''
    Python file to implement the class CrewMate
'''
from custom import comparator_crew
from heap import Heap
class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        self.id = 0
        self.queue = Heap(comparator_crew,[])
        self.no = 0
        self.current_time = 0
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        
        # Write your code here
        
    
    # Add more methods if required
    