def vysokosnyi(year):
    if year>=1 and year<=10000:
        if(not year%4 and year%100) or not year % 400:
            print("YES")
        else:
            print("NO")

year = int(input())
vysokosnyi(year)