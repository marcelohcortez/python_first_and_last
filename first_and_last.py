def find_start(arr, target):
    left, right = 0, len(arr) - 1

    if arr[0] == target:
        return 0
    
    while left <= right:
        mid = ( left + right ) // 2
        if arr[mid] == target and arr[mid-1] < target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
    
def find_end(arr, target):
    left, right = 0, len(arr) - 1

    if arr[-1] == target:
        return len(arr) - 1
    
    while left <= right:
        mid = ( left + right ) // 2
        if arr[mid] == target and arr[mid+1] > target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def find_first_and_last(arr, target):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        print(f'{target} not found.\n')

    start = find_start(arr, target)
    end = find_end(arr, target)

    print(f'It starts in the index {start} and ends in the index {end}\n')

if __name__ == '__main__':
    target = 6
    arr = [1,3,5,5,5,6,6,6,6,6,6,6,7,9,16,20,26,26,50,89]

    find_first_and_last(arr, target)