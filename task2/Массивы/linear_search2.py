size = int(input())
if abs(size)<=1000:
    array = list(map(int,input().split()))
    search_number = int(input())
    if abs(search_number)<=1000:
        result = array.count(search_number)
        if result>0:
            print('YES')
        else:
            print('NO')
