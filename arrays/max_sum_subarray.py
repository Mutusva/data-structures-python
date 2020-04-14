from functools import reduce

arr = [1, 8, 6, 6, 1, 4, 3, 1, 0, 0, 7, 8]
sum = 15

# JavaScript Arrow Function
#const square = number => number * number;
#Python Lambda Expression
square = lambda number: number * number

# Map, Filter, and Reduce

numbers = [1,2,3,4,5,6]
odd_numbers = filter(lambda n: n % 2 == 1, numbers)
squared_odd_numbers = map(lambda n: n * n, odd_numbers)
total = reduce(lambda acc, n: acc + n, squared_odd_numbers)

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
print(square(3))
print(total)


 