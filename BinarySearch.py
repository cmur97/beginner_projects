def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False

if __name__ == "__main__":
    arr = [0, 1, 4, 5, 34, 67, 88, 91, 95, 100]
    tar = 91
    print(binary_search(arr, tar))