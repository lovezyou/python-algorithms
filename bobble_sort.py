unsorted_array = [25, 21, 22, 24, 23, 27, 26]                            ##the list that is to be sorted
sorted_array = [1,2,3,4,5,6,7,8,9,10]                                    ##the list for checking algorithms optimisation

def bobble_sort(a_list):
    print (0, a_list)                                                    ##printing the unsorted list as pass 0

    for element in range(len(a_list)-1, 0, -1):                                 ##the loop ranges from n-1 to 0 in backward maner
        count = 0
        for i in range(element):
            if a_list[i] > a_list[i+1]:
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
                print (i+1, a_list)                            ##after each iteration list is printed
                count += 1

        if count == 0:                                                   ##for checking if the first iner loop swaped any values
            return a_list
    return a_list

print ("unsorted array is passed to the function:")
print ("sorted array : ",bobble_sort(unsorted_array))

print ("\nsorted array is passed to the function:")
print ("sorted array : ",bobble_sort(sorted_array))
