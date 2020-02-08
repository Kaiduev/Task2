# def maxAge_minAge(a, b, c):
#     all_guys = {
#         1: 'Anton',
#         2: 'Boris',
#         3: 'Victor',
#     }
#     if a > b and a > c:
#         print(all_guys[1])
#     elif b > a and b > c:
#         print(all_guys[2])
#     elif c > a and c > b:
#         print(all_guys[3])
#     elif a == b and b == c:
#         print("Same age")
#     elif a == b and a > c:
#         print(all_guys[3])
#     elif b == a and b > c:
#         print(all_guys[3])
#     elif c == b and c > a:
#         print(all_guys[1])
#     elif b == c and b > a:
#         print(all_guys[1])
#     elif c == a and a > b:
#         print(all_guys[2])
#     elif a == c and c > b:
#         print(all_guys[2])
#
#     maxAge_minAge(a, b, c)

a, b, c = map(int, input().split())
all_guys = {
    1: 'Anton',
    2: 'Boris',
    3: 'Victor',
}
if a > b and a > c:
    print(all_guys[1])
elif b > a and b > c:
    print(all_guys[2])
elif c > a and c > b:
    print(all_guys[3])
elif a == b and b == c:
    print("Same age")
elif a == b and a > c:
    print(all_guys[3])
elif b == a and b > c:
    print(all_guys[3])
elif c == b and c > a:
    print(all_guys[1])
elif b == c and b > a:
    print(all_guys[1])
elif c == a and a > b:
    print(all_guys[2])
elif a == c and c > b:
    print(all_guys[2])