def Season(month_number):
    all_seasons = {
        1: 'Winter',
        2: 'Spring',
        3: 'Summer',
        4: 'Autumn',
    }
    if  month_number>=1 and month_number<=2:
        return all_seasons[1]
    elif month_number>=3 and month_number<=5:
        return all_seasons[2]
    elif month_number>=6 and month_number<=8:
        return all_seasons[3]
    elif month_number>=9 and month_number<=11:
        return all_seasons[4]
    elif month_number==12:
        return all_seasons[1]
    else:
        return "Wrong number"



month_number = int(input())
all_seasons = {
        1: 'Winter',
        2: 'Spring',
        3: 'Summer',
        4: 'Autumn',
    }
if  month_number>=1 and month_number<=2:
    print(all_seasons[1])
elif month_number>=3 and month_number<=5:
    print(all_seasons[2])
elif month_number>=6 and month_number<=8:
    print(all_seasons[3])
elif month_number>=9 and month_number<=11:
    print(all_seasons[4])
elif month_number==12:
    print(all_seasons[1])
else:
     print("Wrong number")
