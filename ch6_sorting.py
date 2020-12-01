def selection_sort(A):
    n = len(A)
    for k in range(n):
        minimal = k
        for j in range(k + 1, n):
            if A[j] < A[minimal]:
                minimal = j
        A[k], A[minimal] = A[minimal], A[k]  # swap A[k] and A[minimal]

    return A


def counting_sort(A, k):
    n = len(A)
    count = [0] * (k + 1)

    for i in range(n):
        count[A[i]] += 1
        p = 0
        for i in range(k + 1):
            for j in range(count[i]):
                A[p] = i
                p += 1
        return A

def merge_sort(A, l, r):

    pass

if __name__ == "__main__":

    import copy
    A = [2, 7, 6, 5, 99, 4]

    selection_sorted_A = selection_sort(copy.deepcopy(A))

    print(f"A: {A} Selection Sorted A:{selection_sorted_A}")

    counting_sorted_A = counting_sort(copy.deepcopy(A), len(copy.deepcopy(A))+1)

    print(f"A: {A} Counting Sorted A:{counting_sorted_A}")
