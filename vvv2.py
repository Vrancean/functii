def lista_integer():
    n=int(input("Numarul e elemente este:"))
    l=[]
    for i in range(n):
        element=int(input())
        l.append(element)
    return l
l1=lista_integer()
print("Lista de integer este ",l1)