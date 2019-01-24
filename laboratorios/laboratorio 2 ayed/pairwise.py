def pairwise(lista):
    
    if len(lista)==2:
        return lista[0]*lista[1]
    else:
        if lista[0]<lista[1]:
            k=lista[0]
            n=lista[1]
            return pairwise(lista[1:])
        if lista[O]>lista[1]:
            n=lista[0]
            return pairwise(lista)
        return n*k
        
def main():
    lista=[6,8,12,1,3]
    lista.sort()
    print(pairwise(lista))
main()
    
        
        
        
        
