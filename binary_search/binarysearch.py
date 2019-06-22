# Implementation binary search method
# Returns index of searchValue in sortedArray if present, else -1


def binarySearch(searchValue, sortedArray):

    if not sortedArray:
        return -1
    maxIndex = len(sortedArray)
    minIndex = 0
    while maxIndex > minIndex:
        midIndex = minIndex + ((maxIndex - minIndex) // 2)
        if searchValue == sortedArray[midIndex]:
            return midIndex
        if searchValue > sortedArray[midIndex]:
            minIndex = midIndex + 1
        else:
            maxIndex = midIndex
    return -1

#test
test_array = [1, 3, 5, 7, 9, 11]
value = 9

# Function call
result = binarySearch(value, test_array)

if result != -1:
    print("Search value ", value, "is present at index", result)
else:
    print("Search value ", value, " is not present in array")

