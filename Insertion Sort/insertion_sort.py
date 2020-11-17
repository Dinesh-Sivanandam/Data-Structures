#function for insertion sort
def insertion_sort(elements):
    #taking the elements one by one
    #placing the anchor element as 1st element
    #then the previous value as j
    #and checking the condition in loop as j <=0 and value of anchor < element[j]
    #if so the value is less and we need to swap those two elements and the loop continues by checking the previous elements
    #else we are making the anchor element as j+1 for next iteration
    #finally our array is sorted
    #is it not efficient for long arrays as it has O(n2)
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor

#starting the main
if __name__ == '__main__':
    
    #creating elements for many test cases
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    #taking elements one by one and performin the sorting
    for elements in tests:
        insertion_sort(elements)
        print(f'sorted array: {elements}')
