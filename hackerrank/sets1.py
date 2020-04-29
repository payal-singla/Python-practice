def average(array):
    array1=set(array)
    avg=float(sum(array1)/len(array1))
    return avg
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)