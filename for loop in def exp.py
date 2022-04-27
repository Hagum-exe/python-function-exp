# this def uses a FOR LOOP and returns sum of all FOREACH values

def fordef():               #def without argument
    sum = 0
    for counter in range (2, 8):  #loops from 1 to 4
        print('counter is:',counter )
        sum = sum+counter
        
        if counter==5:
            break
         
            
    return sum
    
#main program        
fordef()




        