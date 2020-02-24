
def num_ways(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return num_ways(n-1) + num_ways(n-2)


print(num_ways(26))
