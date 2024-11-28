'''
    This file contains the class definition for the StrawHat class.
'''
from crewmate import CrewMate
from heap import Heap
from treasure import Treasure
from custom import comparator_crew as comparator2
from custom import comparator_crewmate_straw as comparator

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        self.total_waiting = 0
        self.crew = Heap(comparator,[])
        self.crew2_useful = Heap(comparator,[])
        self.active = 0
        self.no_crewmates = m
        for i in range(m):
            req = CrewMate()
            self.crew.insert(req)
        
        # Write your code here
        pass
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        Toadd:CrewMate = self.crew.top()
        treasure1:Treasure = treasure
        # treasure1.waits('prior',0)
        info = treasure1.arrival_time - Toadd.current_time
        if(Toadd.id>= info):
            Toadd.id = Toadd.id-info + treasure1.size
        else:
            Toadd.id =  treasure1.size

        Toadd.current_time = treasure1.arrival_time
        Toadd.queue.insert(treasure1)
        Toadd.no +=1
        if(self.active <self.no_crewmates):
            self.active +=1
            self.crew2_useful.insert(Toadd)
        self.crew.heapify_down(0)
        # Write your code here
        
    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        list1 = []
        lis = self.crew.heap
        if(self.active<self.no_crewmates):
            lis = self.crew2_useful.heap
        for j in range(len(lis)-1,-1,-1):
            crew:CrewMate = lis[j]
            no_obj = crew.no
            self.total_waiting = 0
            treasure_list = []
            delay = 0
            min_arrival = crew.current_time
            for i2 in range(no_obj):
                chest:Treasure = crew.queue.extract()
                treasure_list.append(chest)
                if(self.total_waiting ==0):
                    chest.completion_time = chest.size
                    delay +=chest.size
                    chest.completion_time += chest.arrival_time
                    self.total_waiting += chest.size + chest.arrival_time
                    
                    min_arrival = chest.arrival_time

                else:
                    if(chest.arrival_time < min_arrival):
                        chest.completion_time = (chest.size+abs(chest.arrival_time - self.total_waiting)) - (min_arrival- chest.arrival_time)
                        chest.completion_time += chest.arrival_time
                    else:
                        
                         
                        if(chest.arrival_time - self.total_waiting >=0):
                            chest.completion_time = chest.size + chest.arrival_time
                        else:
                            load = 0
                            req = max(delay-(chest.arrival_time - min_arrival),0)#error when there is a time gap then calc will be wrong
                            a = (chest.arrival_time - min_arrival)
                            for i in treasure_list:
                                if(i.completion_time != None and i.completion_time<chest.arrival_time):
                                        load+= i.size
                                elif(load<a and i.arrival_time<chest.arrival_time):
                                        load = min(load+i.size,chest.arrival_time - min_arrival)        
                                else:
                                        break    
                            req = delay - load 
                            chest.completion_time = chest.size+req
                            chest.completion_time += chest.arrival_time
                    min_arrival = min(min_arrival,chest.arrival_time)
                    delay += chest.size
                    self.total_waiting = chest.completion_time  
                if(i2 < no_obj-1):
                    crew.queue.top().__class__.wait = chest.completion_time 

                crew.queue.heapify_down(0)       
                list1.append(chest)
                list1[0].__class__.wait = 0    
            crew.queue = Heap(comparator2,treasure_list)    
        list1.sort( key=lambda x: x.id)
        # Write your code here
        return list1
        # Write your code here
        
    
    # You can add more methods if required




#     '''
#     This file contains the class definition for the StrawHat class.
# '''