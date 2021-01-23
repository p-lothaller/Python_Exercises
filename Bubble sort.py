

# A function receiving a list of integers as input
# and sorting them in increasing order using bubble sort.
def bubble_sort(xs):
    x = 0
    while len(xs) != x:
        for i in range(len(xs)-x-1):
            if xs[i] < xs[i+1]:
                pass
            else:
                (xs[i],xs[i+1]) = (xs[i+1],xs[i])
        x+=1
    return xs


xs = [2, 1, 3, 8, 4, 5, 6, 7]
bubble_sort(xs)
