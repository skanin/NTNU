global maximum


def _lis(arr , n ):

    # to allow the access of global variable
    global maximum

    # Base Case
    if n == 1 :
        return 1

    # maxEndingHere is the length of LIS ending with arr[n-1]
    maxEndingHere = 1

    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2] 
       IF arr[n-1] is maller than arr[n-1], and max ending with 
       arr[n-1] needs to be updated, then update it"""
    for i in range(1, n):
        res = _lis(arr , i)
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
            maxEndingHere = res +1
        print(i)

    # Compare maxEndingHere with overall maximum. And
    # update the overall maximum if needed
    maximum = max(maximum , maxEndingHere)

    return maxEndingHere

def lis(arr):
    n = len(arr)

    # Declare the list (array) for LIS and initialize LIS
    # values for all indexes
    lis = [1]*n

    # Compute optimized LIS values in bottom up manner
    for i in range (1 , n):
        for j in range(0 , i):
            if arr[i][1] >= arr[j][1] and arr[i][0] != arr[i][0] and lis[i]< lis[j] + 1 :
                lis[i] = lis[j]+1
        print(i)
    # Initialize maximum to 0 to get the maximum of all
    # LIS
    maximum = 0

    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum , lis[i])

    return maximum


arr = list(map(int, open('input-vekksort2.txt', 'r').read().split('\n')))
print("Length is", lis(arr))