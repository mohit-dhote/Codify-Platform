def partition(arr, beg, end):
    left, right, temp, loc, flag = 0, end, arr[beg], beg, 0
    while flag != 1:
        while (arr[loc] <= arr[right]) and (loc != right):
            right -= 1
        if loc == right:
            flag = 1
        else:
            temp = arr[loc]
            arr[loc], arr[right] = arr[right], arr[loc]
            loc = right
    while (arr[loc] >= arr[left]) and (loc != left):
        left += 1
    if loc == left:
        flag = 1
    else:
        temp = arr[loc]
        arr[loc], arr[left] = arr[left], arr[loc]
        loc = left
    return loc

def quick_sort(arr, beg, end):
    if beg < end:
        loc = partition(arr, beg, end)
        print("\nThe array after partition:")
        for i in range(beg, end + 1):
            print(arr[i], end=" ")
        print()
        quick_sort(arr, beg, loc - 1)
        print("\nThe array after left sub-array sorted is:")
        for i in range(beg, loc):
            print(arr[i], end=" ")
        print()
        quick_sort(arr, loc + 1, end)
        print("\nThe array after right sub-array sorted is:")
        for i in range(loc + 1, end + 1):
            print(arr[i], end=" ")
        print()

def main():
    n = int(input("Enter number of elements in the array: "))
    arr = [int(input(f"Enter element {i + 1}: ")) for i in range(n)]
    print("\nThe unsorted array is:")
    for i in range(n):
        print(arr[i], end=" ")
    quick_sort(arr, 0, n - 1)
    print("\nThe sorted array is:")
    for i in range(n):
        print(arr[i], end=" ")

if __name__ == "__main__":
    main()
