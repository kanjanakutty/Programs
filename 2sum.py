#two sum of two numbers

def two_sum(arr,sum):
    arr.sort()
    left=0
    right=len(arr)-1
    while (left<=right):
        if (arr[left]+arr[right]>sum):
            right=right-1
        elif (arr[left]+arr[right] < sum):
            left=left+1
        elif (arr[left]+arr[right]==sum):
            print("values of pair ", arr[left], "&", arr[right])
            right = right-1
            left = left + 1

arr=[2,4,7,1,8,6]
sum=9

two_sum(arr,sum)
