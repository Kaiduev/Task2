# def triange(a,b,c):
#     if a > 0 and b > 0 and c > 0:
#         if (a+b+c) == 180:
#             print("YES")
#         else:
#             print("NO")
#     else:
#         print("NO")
#
# while True:
#     a, b, c = map(int, input().split())
#     triange(a, b, c)
while True:
    a, b, c = map(int, input().split())
    if a > 0 and b > 0 and c > 0:
        if (a+b+c) == 180:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
