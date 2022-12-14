def trocarAB(a, b):
    print(b, a)

for i in range(5):
    a, b = map(int, input().split())
    trocarAB(a, b)

