def is_perfect_number(number):
    for i in range(2, number):
        if number%i==0:
            print('YES')
            break
        else:
            print('NO')
            break

n = int(input())
if n>=1 and n<=pow(10,9):
    is_perfect_number(n)