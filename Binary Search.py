# Program to state binary search algorithm :
# at line 9 using () is crucial , otherwise value will change.
arr=[7,4,2,9,19,11,14]
arr.sort()
start=0
end=len(arr)-1
x=9
while(start<=end):
    mid=(start+end)//2
    
    if(arr[mid]<x):
        start=mid+1
    else:
        print("element found at",mid)
        break
else:
    print("element not found")




    

        
    
