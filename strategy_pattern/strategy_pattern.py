from abc import ABC, abstractclassmethod


class SortInterface(ABC):
    """
    Strategy interface class. Establishes API for concrete algorithms.
    Note, in Python you can easily implement this pattern with functions
    instead of classes, which can make the implementation a little more light
    weight.
    """

    @abstractclassmethod
    def sort(self, array):
        pass


class MergeSorter(SortInterface):
    """
    Good algorithm to use when dataset is very large or when working with data that is not all in working memory.
    """

    def sort(self, arr):
        print("Using merge sort!")
        self.mergeSort(arr)

    def mergeSort(self, arr):
        if len(arr) > 1:
            # Finding the mid of the array
            mid = len(arr) // 2

            # Dividing the array elements
            L = arr[:mid]

            # Into 2 halves
            R = arr[mid:]

            # Sorting the first half
            self.mergeSort(L)

            # Sorting the second half
            self.mergeSort(R)

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1


class QuickSorter(SortInterface):
    """
    Good for when dataset is fully in memory.
    """

    def partition(self, array, low, high):
        # choose the rightmost element as pivot
        pivot = array[high]

        # pointer for greater element
        i = low - 1

        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if array[j] <= pivot:
                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1

                # Swapping element at i with element at j
                (array[i], array[j]) = (array[j], array[i])

        # Swap the pivot element with the greater element specified by i
        (array[i + 1], array[high]) = (array[high], array[i + 1])

        # Return the position from where partition is done
        return i + 1

    def quickSort(self, array, low, high):
        if low < high:
            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pi = self.partition(array, low, high)

            # Recursive call on the left of pivot
            self.quickSort(array, low, pi - 1)

            # Recursive call on the right of pivot
            self.quickSort(array, pi + 1, high)

    def sort(self, array):
        print("Using quick sort!")
        self.quickSort(array, 0, len(array) - 1)


class InsertionSorter(SortInterface):
    """
    Good for when array is already largely in order.
    """

    def sort(self, arr):
        print("Using insertion sort!")
        n = len(arr)  # Get the length of the array

        if n <= 1:
            return  # If the array has 0 or 1 element, it is already sorted, so return

        for i in range(1, n):  # Iterate over the array starting from the second element
            key = arr[
                i
            ]  # Store the current element as the key to be inserted in the right position
            j = i - 1
            while (
                j >= 0 and key < arr[j]
            ):  # Move elements greater than key one position ahead
                arr[j + 1] = arr[j]  # Shift elements to the right
                j -= 1
            arr[j + 1] = key  # Insert the key in the correct position


class DataContext:
    def __init__(self, sort_strategy=None):
        self.sort_strategy = sort_strategy

    def assign_strategy(self, strategy):
        """
        Context needs ability to assign different strategies based on
        what client needs.
        """
        self.sort_strategy = strategy

    def sort_data(self, array):
        """
        Method needs to rely on the strategy interface in function call.
        """
        self.sort_strategy.sort(array)


if __name__ == "__main__":
    data = [5, 3, 2, 6, 1]
    merge_sort = MergeSorter()
    quick_sort = QuickSorter()
    insertion_sort = InsertionSorter()
    print(data)

    # if sorting large dataset, including data written to many files
    context = DataContext(sort_strategy=merge_sort)
    context.sort_data(data)

    # if data fits in memory
    context.assign_strategy(quick_sort)
    context.sort_data(data)

    # if data already largely sorted
    context.assign_strategy(insertion_sort)
    context.sort_data(data)
