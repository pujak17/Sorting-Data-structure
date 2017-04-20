# Integer Ordered Data Generator
# @author: Harpreet Singh Arora
import csv
import sys

def dataOrderGen(dataSize,outputfile):
    with open(outputfile, 'w') as csvfile:
        wr = csv.writer(csvfile,delimiter=",")
        for x in range(dataSize,0,-1):
            wr.writerow([x])

if __name__ == "__main__":
    try:
        dataOrderGen(int(sys.argv[1]),sys.argv[2])
    except (IndexError, ValueError):
        print('usuage %s <data size> [outputfile]' % sys.argv[0])
