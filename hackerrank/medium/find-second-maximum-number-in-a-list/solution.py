if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    champion = (arr[0])
    runner_up = float('-inf')
    for i in range (1,len(arr)):
        if arr[i] > champion:
            runner_up = champion
            champion = arr[i]
        elif  arr[i] > runner_up and arr[i] != champion:
            runner_up = arr[i]
    print(runner_up)
