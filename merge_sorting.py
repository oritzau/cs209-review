
def merge_sort(list):
    merge_sortR(list, 0, len(list) - 1)

# sorts list elements in range of indices sti to endi (inclusive)
def merge_sortR(list, sti, endi):
    if sti >= endi:
        return   # 1 element by itself is already sorted so we are done

    # if sti < endi:
    mididx = (sti + endi) // 2
    merge_sortR(list, sti, mididx)
    merge_sortR(list, mididx + 1, endi)

    # we expect list to be sorted from sti to mididx
    # and from mididx+1 to endi

    temp_list = []
    left_i = sti
    right_i = mididx + 1
    while left_i <= mididx and right_i <= endi:
        if list[left_i] < list[right_i]:
            temp_list.append(list[left_i])
            left_i += 1
        else:
            temp_list.append(list[right_i])
            right_i += 1

    # either the left half is exhausted or the right half is
    if left_i > mididx:
        # left half is exhausted
        # so we copy the remainder on the right into list
        temp_list += list[right_i:endi+1]
    else:
        # right half is exhausted
        # so we copy the remainder on the left into list
        temp_list += list[left_i:mididx+1]

    # in list we have to copy all of temp_list into list[sti:endi+1]
    list[sti:endi+1] = temp_list.copy()


mylist = [12,54,32,44,33,32,65,87,65,-34,5,7,1,20,-90,7]
merge_sort(mylist)
print(mylist)

    
