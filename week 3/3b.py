def insertion_sort(arr):
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key

    return arr


n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input("Enter the element: ")))

print(insertion_sort(arr))