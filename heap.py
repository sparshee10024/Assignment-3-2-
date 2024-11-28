'''
Python Code to implement a heap with general comparison function
'''
from treasure import  Treasure
# def min_comparator(a, b):
#     return a < b

# def comparator(a: Treasure,b: Treasure):
#     maxi = max(a.arrival_time,b.arrival_time)
#     a1 = maxi - (a.arrival_time + a.size)
#     b1 = maxi - (b.arrival_time + b.size)
#     return a1 > b1

class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        # Write your code here
        self.heap: list = init_array[:]
        self.comp = comparison_function
        if init_array:
            self.heapify()
            
        
        
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
        
    
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
          # Move the last element to the root
        # if len(self.heap) == 0:
        #     return
        self.heapify_down(0)
        return root
        # Write your code here

        
    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        # Write your code here
        return self.heap[0]
    
    # You can add more functions if you want to

    def parent(self,i):
        return (i-1)//2
    
    def left_child(self,i:int):
        return 2*i+1
    
    def right_child(self,i:int):
        return 2*i+2
    

    def heapify_up(self,index):
        while index>0:
            parent_idx = self.parent(index)
            if(self.comp(self.heap[index],self.heap[parent_idx])):
                self.heap[index],self.heap[parent_idx] = self.heap[parent_idx], self.heap[index]
                index = parent_idx
            else:
                break  


    def heapify_down(self,index):

        while(self.left_child(index) < len(self.heap)):
            
            left = self.left_child(index)
            right = self.right_child(index)
            # print('done',left,right)

            if(right < len(self.heap) and self.comp(self.heap[right],self.heap[left])):
                smaller = right
            else:
                smaller = left

            if(self.comp(self.heap[smaller],self.heap[index])):
                self.heap[index],self.heap[smaller] = self.heap[smaller], self.heap[index]
                index = smaller
            else:
                break
    def heapify(self):
        # Start from the last non-leaf node and sift down each node
        # Non-leaf nodes are all nodes at indices len(self.heap)//2 - 1 down to 0
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)
            
            
            
            
  



