# Write your function here


def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for i in lst1:
        sum1 += i
    for i in lst2:
        sum2 += i
    if sum1 >= sum2:
        return lst1
    else:
        return lst2


# Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

# Write your function here


def over_nine_thousand(lst):
    sum = 0
    for number in lst:
        sum += number
        if (sum > 9000):
            break
    return sum


# Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

# Write your function here


def max_num(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


# Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

# Write your function here


def same_values(lst1, lst2):
    equal = []
    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            equal.append(i)
    return equal


# Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# Write your function here


def reversed_list(lst1, lst2):
    for i in range(len(lst1)):
        if lst1[i] != lst2[len(lst2) - 1 - i]:
            return False
    return True


# Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
