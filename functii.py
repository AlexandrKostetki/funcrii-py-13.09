from msilib.schema import Error


n=int(input("nr de elemente in lista="))

def listeint(nr):
    lista_loc=[]
    for i in range(nr):
        element=int(input('Elementul'+float(i+1)+'este'))
        lista_loc.append(element)
    return lista
def afisare_lista(x):
    for i in x:
        print(i)
lista1=creare_lista()
afisare_lista(lista1)


        
          
            
    