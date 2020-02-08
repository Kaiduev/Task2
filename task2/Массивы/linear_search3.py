size = int(input())
result = 0
if abs(size)<=1000:
    array = list(map(int,input().split()))
    search_number = int(input())
    if abs(search_number)<=1000:
        try:
            result = array.index(search_number)
        except:
            if result>0:
                print(result+1)