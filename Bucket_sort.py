def insertionSort(data):

    for index in range(1,len(data)):



        currentvalue = data[index]

        i = index



        while i>0 and data[i-1]>currentvalue:

            data[i]=data[i-1]

            i = i-1

        data[i]=currentvalue



def bucket_sort(A):

    n = len(A)

    B = [[] for i in range(n+1)]

    ##print(B)

    #print(int(n*max(A)))

    #print(len(B),B)



    for i in range(n):

        ##print(A[i], n)

        B[int(n*A[i])].append(A[i])



    for i in range(n):

        insertionSort(B[i])

    ##print("----")

    ##print(n)

    C = []

    for i in range(n):

        ##print(len(B[i]))

        for j in range(len(B[i])):

            ##print("B[j]:", B[j])

            ##print("n",n," B:",B[i][j])

            C.append(B[i][j])

    ##print(B)

    ##print(C)

    return C



if __name__ == '__main__':

    print("Bucket_Sort")

    ##print("input : ",data)

    bucket_sort(data)

    ##print("Output : ",data)
