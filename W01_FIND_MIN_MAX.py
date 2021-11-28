def findMinMax(x): 
    
    # define the min and max num 
    n_min = float("inf")
    n_max = float("-inf")
    
    # loop through each element 
    for i in x:
        if i < n_min:
            n_min = i 
        if i > n_max:
            n_max = i 
    
    # return final answer 
    return (n_min, n_max) 

l = [-100, -50, 0, 1, 50, 100]

print(findMinMax(l))