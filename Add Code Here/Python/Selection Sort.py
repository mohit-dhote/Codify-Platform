def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = []
n = int(input("Enter No. of elements you want to sort: "))
print("Enter elements:")
for _ in range(n):
    arr.append(int(input()))

sorted_arr = selection_sort(arr)

print("Sorted list:")
for num in sorted_arr:
    print(num)
