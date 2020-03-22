def counting_sort(A, k):
    output = [0 for i in range(len(A))]
    count = [0 for i in range(k+1)]

    for i in range(len(A)):
        count[A[i]] += 1

    for i in range(0, k):
        count[i+1] += count[i]

    for i in range(len(A)-1, 0, -1):
        output[count[A[i]]] = A[i]

        count[A[i]] -= 1

    return output


a = [4,3,2,1,6,7,87,8,8,7,6,65,5,3,2,1,3,4,5,6]
print(counting_sort(a, max(a)))