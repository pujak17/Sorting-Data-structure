from Mergesort import *
from insertionsort import *
from heapsort import *
from countingsort import *
from radixsort import *
from Bucket_sort import *
import time

current_time = lambda: int(round(time.time()*1000))

datafile = 'R1200.dat'

with open(datafile) as f:
    data = f.read().splitlines()

print(len(data))
##print(data)

data = list(map(int,data))

## Merge Data
data1 = data[:]
## Insertion Data
data10 = data[:]
## selectionsort
data1 = data[:]
## Heap Data
data3 = data[:]
## Counting Data
data4 = data[:]
data5 = data4[:]
## Radix Data
data6 = data[:]
## Bucket Data
data7 = data[:]
data7 = [x / float(len(data7)) for x in data7]
data7 = [float('%.2f' % k) for k in data7]


##Test Bucket Sort
start = current_time()
bucket_sort(data7)
end = current_time()
print("Bucket Sort time : %d mil.seconds" % (end-start))

##Test Merge Sort
start = current_time()
merge_sort(data1,0,len(data1)-1)
end = current_time()
print("Merge Sort time : %d mil.seconds" % (end-start))

##Test Insertion Sort
start = current_time()
insertion_sort(data10)
end = current_time()
print("Insertion Sort time : %d mil.seconds" % (end-start))

##Test Heap Sort
start = current_time()
heapsort(data3)
end = current_time()
print("Heap Sort time : %d mil.seconds" % (end-start))

##Test Counting Sort
start = current_time()
counting_sort(data4,data5,max(data4))
end = current_time()
print("Counting Sort time : %d mil.seconds" % (end-start))

##Test Radix Sort
start = current_time()
radixsort(data6)
end = current_time()
print("Radix Sort time : %d mil.seconds" % (end-start))

