def lista_float():
    n=int(input("Numarul e elemente este:"))
    l=[]
    for i in range(n):
        element=int(input())
        l.append(element)
    return l
l1=lista_float()
print("Lista de float este ",l1)