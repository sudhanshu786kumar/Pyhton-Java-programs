def merge(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        merge(L)
        merge(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if(L[i]<R[j]):
                arr[k]=L[i]
                i=i+1
            else:
                arr[k]=R[j]
                j=j+1
            k=k+1
        while i<len(L):
            arr[k]=L[i]
            k=k+1
            i=i+1
        while j<len(R):
            arr[k]=R[j]
            k=k+1
            j=j+1
