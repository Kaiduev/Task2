# def binary_search(array,X,start,stop):
#     if start>stop:
#         return False
#     else:
#         mid = (start+stop)//2
#         if X==array[mid]:
#             i = i + 1
#             return mid
#         elif X<array[mid]:
#             i = i + 1
#             return binary_search(array,X,start,mid-1)
#         else:
#             i = i + 1
#             return binary_search(array,X,mid+1,stop)
# size,X = map(int,input().split())
# array = list(map(int,input().split()))
# array.sort()
# start = 0
# stop = len(array)
# result = binary_search(array,X,start,stop)
# if result == False:
#     for i in array:
#         print(i,end=' ')
#     print()
#     print('NO')
# else:
#     for i in array:
#         print(i,end=' ')
#     print()
#     print('YES')















