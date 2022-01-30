"""
performing quick sort

"""
def part(arr,l,h):
    piv=arr[h] #pivot last element of array
    point=l-1 #pointer for largest element  which is first  element of array
    for i in range(l,h): #looping the array to compare
        if(arr[i]<=piv): #comparing the array element with th e pivot if elemnt i slower than pivot
            point=+1 # move to the next element as the current will be swaped with smaller element
        (arr[i],arr[point])=(arr[point],arr[i]) #now swapping the number lower than pivot with the pointer of largest element
    (arr[point+1],arr[h])=(arr[h],arr[point+1]) #finally the swap the second last element with the pivot which are not smaller further than that and finally puttin equal number 
    return point+1 # and at final returning the final position at point which is partitoning

def quick(arr,l,h):
    if l<h:
        pi=part(arr,l,h) # finding the pivot such that lower on side of left of pivot and other on right
        quick(arr,l,pi-1)#for left sort
        quick(arr,pi+1,h)#for right sort

