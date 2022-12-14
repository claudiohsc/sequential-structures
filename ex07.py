def maiorAB(a,b):
    if a > b:
        print(a)
    else:
        print(b)
 
contar = 0
while contar <= 4:
    a,b = input().split()
    a = int(a)
    b = int(b)

    maiorAB(a,b)
    contar += 1


