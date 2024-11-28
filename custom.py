# You can add any additional function and class you want to implement in this file
from treasure import *
def comparator_crew(a,b):
    maxi = max(a.arrival_time,b.arrival_time)
    

    a1 = 2*(maxi - a.arrival_time) - a.size
    b1 = 2*(maxi - b.arrival_time) - b.size
    # print("active",a.wait)
    if(a.wait != 0 and (a.arrival_time<a.wait or b.arrival_time<b.wait)):
        add = 0
        a1 = 0
        b1 = 0
        if(maxi != a.arrival_time):
            
            add = max(0,maxi-a.wait)
            a1 = add
        else:
            
            add = max(0,maxi-a.wait)
            b1 = add

            
        a1 += 1*(maxi - a.arrival_time) - a.size
        b1 += 1*(maxi - b.arrival_time) - b.size
        # print("active",a1,b1,a.arrival_time,b.arrival_time)
    if(a1 == b1):
        return a.id <b.id
    return a1 > b1

def comparator_crewmate_straw(a,b):
    maxi = max(a.current_time,b.current_time)
    a1 = (a.current_time- maxi) + a.id
    b1 = (b.current_time - maxi) + b.id
    return a1 < b1