# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here:

        # For every index that hasn't been sorted already
        # find the smallest
        for index in range(cur_index, len(arr)):
            if arr[index] < arr[smallest_index]:
                smallest_index = index

        # TO-DO: swap
        # Your code here
        arr.insert(cur_index, arr.pop(smallest_index))
        

    return arr

# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(selection_sort(arr1))
# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    index = 0
    if len(arr) == 0:
        return []
    while True:
        if index == len(arr) - 1:
            break
        elif arr[index] > arr[index + 1]:
            arr.insert(index, arr.pop(index + 1))
            index = 0
        else:
            index += 1
    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(bubble_sort(arr1))
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
