arr = [1, 8, 6, 6, 1, 4, 3, 1, 0, 0, 7, 8]
sum = 15

def find_max_sub_array(arr, val):
    left = 0
    right = 0
    sum = 0
    result = []
    while(right < len(arr)):
        while(sum <= val):
            sum = sum + arr[right]      
            if sum == val and len(result) < (right - left + 1):
                result.clear()
                result.append(left)
                result.append(right)
            right = right + 1
        
        sum -= arr[left]
        left = left + 1
    return result


print(find_max_sub_array(arr, sum))


 