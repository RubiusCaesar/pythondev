# Write your function here


def append_size(lst):
    lst.append(len(lst))
    return lst


# Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

# Write your function here


def append_sum(lst):
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    return lst


# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

# Write your function here


def larger_list(lst1, lst2):
    if(len(lst1) >= len(lst2)):
        return lst1[-1]
    else:
        return lst2[-1]


# Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# Write your function here


def more_than_n(lst, item, n):
    count = 0
    for x in lst:
        if(lst[x] == item):
            count += 1
    if(count > n):
        return True
    else:
        return False

# OR


def more_than_n(lst, item, n):
    if lst.count(item) > n:
        return True
    else:
        return False


# Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

# Write your function here


def combine_sort(lst1, lst2):
    unsorted = lst1 + lst2
    sortedList = sorted(unsorted)
    return sortedList


# Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

# Write your function here


def every_three_nums(start):
    return list(range(start, 101, 3))


# Uncomment the line below when your function is done
print(every_three_nums(91))

# Write your function here


def remove_middle(lst, start, end):
    return lst[:start] + lst[end+1:]


# Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# Write your function here


def more_frequent_item(lst, item1, item2):
    if lst.count(item1) >= lst.count(item2):
        return item1
    else:
        return item2


# Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# Write your function here


def double_index(lst, index):
    if index >= len(lst):
        return lst
    else:
        new_lst = lst[0:index]
        new_lst.append(lst[index]*2)
        new_lst = new_lst + lst[index+1:]
        return new_lst


# Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

# Write your function here


def middle_element(lst):
    if len(lst) % 2 == 0:
        sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
        return sum / 2
    else:
        return lst[int(len(lst)/2)]


# Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
