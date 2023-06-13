import math


class Unsorted_Data:
    def __init__(self, data):
        self.list = data

    def bubble_sort(self):
        # Compares adjacent elements and swap them based on condition
        # In-Place solution
        for i in range(len(self.list)-1):
            for j in range(len(self.list)-1-i):
                if self.list[j] > self.list[j+1]:
                    temp = self.list[j]
                    self.list[j] = self.list[j + 1]
                    self.list[j + 1] = temp

    def selection_sort(self):
        # Assumes the current element is min/max. Searches for min/max in rest of the list and swaps
        # In-Place Solution
        for i in range(len(self.list)):
            index_of_min = i
            for j in range(i+1, len(self.list)):
                if self.list[j] < self.list[index_of_min]:
                    index_of_min = j
            self.list[i], self.list[index_of_min] = self.list[index_of_min], self.list[i]

    def insertion_sort(self):
        # Starting from the 2nd element, keep shifting the element to left whilst its bigger that left elements
        # In-Place Solution

        for i in range(1, len(self.list)):
            temp_value = self.list[i]

            for j in range(i-1, -1, -1):

                if temp_value < self.list[j]:
                    self.list[j+1] = self.list[j]
                    self.list[j] = temp_value
                else:
                    break

    def bucket_sort(self):
        # Create buckets and move elements in appropriate buckets
        # Sort Buckets individually
        # merge all the buckets
        number_of_buckets = round(math.sqrt(len(self.list)))
        buckets = [[] for i in range(number_of_buckets)]
        max_item = max(self.list)

        for item in self.list:
            destination_bucket = math.ceil(item*number_of_buckets/max_item)
            buckets[destination_bucket-1].append(item)

        self.list = []
        for bucket in buckets:
            print(bucket)
            bucket.sort()
            self.list.extend(bucket)

    def bucketSort(self):
        bucket = []

        # Create empty buckets
        for i in range(len(self.list)):
            bucket.append([])

        # Insert elements into their respective buckets
        for j in self.list:
            index_b = int(10 * j)
            bucket[index_b].append(j)

        # Sort the elements of each bucket
        for i in range(len(self.list)):
            bucket[i] = sorted(bucket[i])

        # Get the sorted elements
        k = 0
        for i in range(len(self.list)):
            for j in range(len(bucket[i])):
                self.list[k] = bucket[i][j]
                k += 1

    def merge_sort(self):
        # divide and conquer approach

        def merge_helper(array):
            if len(array) > 1:
                middle = len(array)//2
                left_side = array[:middle]
                right_side = array[middle:]

                merge_helper(left_side)
                merge_helper(right_side)

                i = j = index = 0

                while i < len(left_side) and j < len(right_side):
                    if left_side[i] < right_side[j]:
                        array[index] = left_side[i]
                        i += 1
                    else:
                        array[index] = right_side[j]
                        j += 1
                    index += 1

                while i < len(left_side):
                    array[index] = left_side[i]
                    i += 1
                    index += 1

                while j < len(right_side):
                    array[index] = right_side[j]
                    j += 1
                    index += 1

        merge_helper(self.list)


    def quick_sort(self):

        def quick_sort_helper(array):
            if len(array) <= 1:
                return array
            else:
                pivot = array[0]
                less_than = [item for item in array[1:] if item < pivot]
                more_than = [item for item in array[1:] if item > pivot]
                return quick_sort_helper(less_than) + [pivot] + quick_sort_helper(more_than)

        self.list = quick_sort_helper(self.list)

    def quick_sort_alternate(self):

        def partition(array, start, end):
            pivot = array[end]
            pointer = start -1
            for i in range(start, end):
                if array[i] < pivot:
                    pointer += 1
                    array[pointer], array[i] = array[i], array[pointer]
            array[pointer + 1], array[end] = array[end], array[pointer + 1]

            return pointer + 1


        def quick_sort_helper(array, start, end):
            if start < end:
                pi = partition(array, start, end)
                quick_sort_helper(array, start, pi - 1)
                quick_sort_helper(array, pi + 1, end)

        quick_sort_helper(self.list, 0, len(self.list) -1)


    def heap_sort(self):

        def heapify(arr, n, i):
            # Find largest among root and children
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and arr[i] < arr[l]:
                largest = l

            if r < n and arr[largest] < arr[r]:
                largest = r

            # If root is not largest, swap with largest and continue heapifying
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)


        arr = self.list
        n = len(arr)

        # Build max heap
        for i in range(n // 2, -1, -1):
            heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            # Swap
            arr[i], arr[0] = arr[0], arr[i]

            # Heapify root element
            heapify(arr, i, 0)



a = Unsorted_Data([9,7,8,6,4,5,1,2,3,0])
a.bubble_sort()
print("bubble sort" + str(a.list))

b = Unsorted_Data([9,7,8,6,4,5,1,2,3,0])
b.selection_sort()
print("selection sort" + str(b.list))

c = Unsorted_Data([9,7,8,6,4,5,1,2,3,0])
c.insertion_sort()
print("insertion sort " + str(c.list))

d = Unsorted_Data([9,7,8,6,4,5,1,2,3,0])
d.bucket_sort()
print("bucket sort " + str(d.list))

e = Unsorted_Data([0,0.9,0.7,0.8,0.6,0.4,0.5,0.1,0.2,0.3])
e.bucketSort()
print("bucket sort " + str(e.list))

f = Unsorted_Data([9,7,8,6,4,5,1,2,3,0])
f.merge_sort()
print("merge sort " + str(f.list))

g = Unsorted_Data([9,7,8,6,4,5,1,2,3,0])
g.quick_sort()
print("quick sort " + str(g.list))

h = Unsorted_Data([9,7,8,6,4,5,1,2,3,0])
h.quick_sort_alternate()
print("quick sort alt " + str(h.list))

i = Unsorted_Data([9,7,8,6,4,5,1,2,3,0,11])
i.heap_sort()
print("heap sort alt " + str(i.list))


