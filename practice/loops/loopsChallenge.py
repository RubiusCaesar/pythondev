# Write your function here


def divisible_by_ten(nums):
    count = 0
    for num in nums:
        if (num % 10) == 0:
            count += 1
    return count


# Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

# Write your function here


def add_greetings(names):
    new_names = []
    for name in names:
        new_names.append("Hello, " + name)
    return new_names


# Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

# Write your function here


def delete_starting_evens(lst):
    while (len(lst) > 0 and lst[0] % 2 == 0):
        lst = lst[1:]
    return lst


# Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# Write your function here


def odd_indices(lst):
    odd_lst = []
    for index in range(1, len(lst), 2):
        odd_lst.append(lst[index])
    return odd_lst


# Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

# Write your function here


def exponents(bases, powers):
    exponents = []
    for base in bases:
        for power in powers:
            exponents.append(base**power)
    return exponents


# Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))
