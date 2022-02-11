# determine a cap that will ensure the sum of an array is equal to k while affecting the fewest number of elements
def find_cap(elements, k):
    if sum(elements) < k:
        return len(elements)
    cap = len(elements)
    while cap > 0:
        if sum(elements[:cap]) == k:
            return cap
        cap -= 1
    return 0