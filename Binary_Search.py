def binarysearch(item, myList):
    found = False
    found_index = -1
    lowerBound = 0
    upperBound = len(myList) - 1

    while lowerBound <= upperBound and found == False:
        mid = (lowerBound + upperBound)//2
        if myList[mid] == item:
            found_index = mid
            found = True
        elif myList[mid] < item:
            lowerBound = mid + 1
        elif myList[mid] > item:
            upperBound = mid - 1
        else: 
            found_index = -1
    return found_index



#list should be in ascending order
myList = [-11, 0, 5, 99]
item = int(input("Item to be searched:\n"))

result = binarysearch(item, myList)

if result != -1:
    print("Item has been found at index {}".format(result))
else:
    print("Item NOT found")
    