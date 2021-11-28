def plusMinus(arr):
    # initialize 
    pos = 0
    neg = 0
    zer = 0
    length = len(arr) 
    
    # loop through each element in array 
    for n in arr:
        if n > 0:
            pos += 1 
        elif n == 0:
            zer += 1 
        else: 
            neg += 1 
    
    print(pos / length) 
    print(neg / length) 
    print(zer / length)

# Call the function
plusMinus([-3, -2, -1, 0, 1, 2, 3])