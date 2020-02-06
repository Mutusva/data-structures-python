
nums = [5, 4, 6, 3, 7, 2, 1, 8]

unsorted = [5, 4, 6, 3, 7, 2, 1, 8]

def printArray(arr):
    for i in range(0, arr.__len__()):
        print(arr[i])

print("----------------Unsorted---------------------------")
printArray(nums)


def mergeSort(arr):
    
    if arr.__len__() <= 1 :
        return arr

    result = []
    left = []
    right = []
    
    arr_length = arr.__len__()
    mid = arr_length / 2   

    for i in range(0, mid):
        left.append(arr[i])
    for j in range(mid, arr_length):
        right.append([arr[j]])
    
    left = mergeSort(left)
    right = mergeSort(right)

    result = merge(left, right)
    return result

def merge(left, right):
    result = []

    leftIndex = 0
    rightIndex = 0

    while(leftIndex < left.__len__() or rightIndex < right.__len__()):

        if leftIndex < left.__len__() and rightIndex < right.__len__():
            if left[leftIndex] <= right[rightIndex]:
                result.append(left[leftIndex])
                leftIndex = leftIndex + 1
            else:
                result.append(right[rightIndex])
                rightIndex = rightIndex + 1
        elif leftIndex < left.__len__():
             result.append(left[leftIndex])
             leftIndex = leftIndex + 1
        elif rightIndex < right.__len__():
            result.append(right[rightIndex])
            rightIndex = rightIndex + 1
    return result

print("----------------sorted---------------------------")
sortedArr = mergeSort(nums)
printArray(sortedArr)
            





    

    
    
