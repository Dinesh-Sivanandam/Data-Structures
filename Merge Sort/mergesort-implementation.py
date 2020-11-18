#function for merge sort
"""
    we are using recursion for seperating the left and right values in the arrays for sorting
    after seperating leeft and right values we are merging the two sorted list
"""
def merge_sort(arr):
    #if len is less than or equal to 1 just returning the array
    if len(arr) <= 1:
        return

    #else we are taking the mid value and creating the left and right array
    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    #calling the function for sorting the left and right
    merge_sort(left)
    merge_sort(right)

    #calling the function for merging the two sorted arrays
    merge_two_sorted_lists(left, right, arr)

#function for merging two sorted list
def merge_two_sorted_lists(a,b,arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0
    """
        if the i and j less than len_a and len_b 
            we are comparing the values in the two arrays
            if less we are making the value to the index from starting and incrementing the index after placing
            else placing the other element in other array
    """
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1

    #after placing the array if there are any other elements left placing the values
    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1

if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    for arr in test_cases:
        merge_sort(arr)
        print(arr)
