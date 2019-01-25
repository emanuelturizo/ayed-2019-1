def m(n,lista):
    j=0
    for h in range(len(lista)):
        for i in range(len(lista)):
            if lista[h]==lista[i]:
                j+=1

    if j > n//2:
        return True
    else:
        return False
def main():
    lista=[2,3,9,2,2]
    n=len(lista)
    print(m(n,lista))
main()
