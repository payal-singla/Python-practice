def is_leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return 'True'
            else:
                return 'False'
        else:
             return 'True'
    return 'False'


    
    # Write your return leap

year = int(input())
print(is_leap(year))