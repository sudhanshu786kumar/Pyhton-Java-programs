def bubble(arr,l):
  for i in range(l):
    for j in range(0,l-i-1):
      if(arr[j]>arr[j+1]):
        temp=arr[j]
        arr[j]=arr[j+1]
        arr[j+1]=temp
  for k in range(l):

    print(arr[k])
