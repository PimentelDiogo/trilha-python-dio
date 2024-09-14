lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()
l2[0] = 99
print(lista)  # [1, "Python", [40, 30, 20]]
print(l2)  # [99, "Python", [40, 30, 20]]