data = [5,2,4,6,1,3,2,6]



def merge(A,p,q,r):

    n1 = q - p + 1

    n2 = r - q

    L = []

    R = []



    for i in range(0,n1):

        #L[i] = A[p + i - 1]

        L.append(A[p+i])

                 

    for j in range(0,n2):

        #R[j] = A[q + j]

        R.append(A[q+j+1])

        

    L.append(float('inf'))

    R.append(float('inf'))

    i = 0

    j = 0

    for k in range(p,r+1):

        if L[i] <= R[j]:

            A[k] = L[i]

            i = i + 1

        else:

            A[k] = R[j]

            j = j + 1

    

def merge_sort(A,p,r):

  q = ((len(data))/2)  

  if p < r:

      q = int((p+r)/2)

      merge_sort(A,p,q)

      merge_sort(A,q+1,r)

      merge(A,p,q,r)

      

if __name__ == '__main__':

    print("Merge_sort")

    ##print("input : ",data)

    merge_sort(data,0,len(data)-1)

    ##print("Output : ",data)
