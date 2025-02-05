
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
my_array = sorted(set(arr))
    
if len(my_array) > 1:
        print(my_array[-2])
    




