from re import L


def selection(arr,l):
    for i in range(l):
        min_s=i #choosing first element as minimum
        for j in range(i+1,l): # loop will start from second element as first is set as minumum
            if(arr[j]<arr[min_s]): #comaparison from 2nd to end element of loop with minimum set earlier
                min_s=j # setting our new small element if found smaller than earlier element
        (arr[min_s],arr[i])=(arr[i],arr[min_s]) # 
    for k in range(l):
        print(arr[k])

#this is a greedy algorithm