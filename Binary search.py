def binary_search(lst, target):
    if len(lst) == 0:
        return -1
    midpoint = (len(lst))//2
    if lst[midpoint] == target:
        return midpoint
    else:
        offset = 0
        if target >= lst[midpoint]:
            offset = midpoint + 1
            index = binary_search(lst[midpoint+1:], target)
        else:
            index = binary_search(lst[:midpoint], target)

        if index != -1:
            return offset + index
        else:
            return -1
                

lst = [0, 2, 4, 5, 7, 8, 9]
binary_search(lst, 9)
