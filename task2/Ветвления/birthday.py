def search_day(day, month):
    all_day = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    if(month-2) > 0:
        month = month-2
    else:
        12-abs(month-2)
    c = 2020 // 100
    y = 2020 % 100
    n = (day + ((13 * month -1) // 5) + y + (y // 4 + c // 4 - 2 * c+777)) % 7
    return all_day[n]

while True:
    d, m = map(int, input().split())
    print(search_day(d, m))
