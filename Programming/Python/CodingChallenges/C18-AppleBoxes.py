def function(k):
    sumodd = 0 #Yellow Apples
    sumeven = 0 #Red Apples
    for i in range(1,k+1):
        if i % 2 == 0:
            sumeven += i * i
        else:
            sumodd += i * i
    
    #Red Apples - Yellow Apples
    return sumeven - sumodd

for x in range(1,10):
    print(function(x))
    
        
