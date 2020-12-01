def main():
    f = open("day1.txt", "r")
    lst = [int(x) for x in f]
    nums = find_nums_that_add_to_2020_hs(lst)
    print(nums)

# Brute Force - triplets
def find_nums_that_add_to_2020_triplets_bf(lst):  
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                if lst[i] + lst[j] + lst[k] == 2020:
                    return [lst[i], lst[j], lst[k]]
    return -1

# Brute Force - pairs
def find_nums_that_add_to_2020_triplets_bf(lst):  
    for i in range(len(lst)):   
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == 2020:
                return [lst[i], lst[j]]
    return -1

# Hashing - pairs
def find_nums_that_add_to_2020_hs(lst):
    saved_values = {}
    for i in range(len(lst)):
        if (2020 - lst[i]) in saved_values:
            return [lst[i], 2020 - lst[i]]
        else:
            saved_values[lst[i]] = i   
    return -1


if __name__ == '__main__':
    main()