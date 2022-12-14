def age(days):
    year = days // 360
    days = days % 360
    month = days // 30
    days = days % 30
    print(f'{year} ano(s), {month} mes(es) e {days} dia(s)')

a, b, c = [int(x) for x in input().split()]

age(a)
age(b)
age(c)
