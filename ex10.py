def age(days):
    year = days // 360
    days = days % 360
    month = days // 30
    days = days % 30
    print(year, month, days)

a, b, c = [int(x) for x in input().split()]

age(a)
age(b)
age(c)
