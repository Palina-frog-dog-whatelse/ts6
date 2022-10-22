def create_massiv(m):
    size = (int(input("Введите размер массива " + m + " ")))
    massiv = []
    for i in range(0,size):
        massiv.append((input("Введите один элемен массива " + m + " " )))
    return massiv
massiv_A = create_massiv("A")
massiv_B = create_massiv("B")
ans = list(set(massiv_A).intersection(massiv_B))
print(ans)
        
