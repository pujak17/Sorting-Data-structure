def countingSort(A, j):

    c = [0]*10

    for i in range(len(A)):

        c[(int)((A[i]/(10**j))%10)] += 1

    for k in range(1,len(c)):

        c[k] += c[k-1]

    B = [0]*len(A)

    for i in range(len(A)-1, -1, -1):
        B[c[(int)((A[i]/(10**j))%10)]-1] = A[i]

        c[(int)((A[i]/(10**j)%10))] -= 1

    A[:] = B[:]



def radixsort(A):

    x = max(A)

    d = 0

    while x != 0:

        d += 1

        x /= 10

    for j in range(d):

        countingSort(A,j)



if __name__ == '__main__':

    print("Radix_Sort")

    ##print("input : ",data)

    radixsort(data)

    ##print("Output : ",data)
