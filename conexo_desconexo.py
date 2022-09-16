from random import randint

visitados= []
pilha= []

grafo = {
    'V1': ['V6', 'V5', 'V2'],
    'V2': ['V1', 'V3'],
    'V3': ['V2', 'V4'],
    'V4': ['V5', 'V3', 'V6'],
    'V5': ['V4', 'V1'],
    'V6': ['V4', 'V1']
}

def visitar(ultimodapilha):    
        remove_visitado()
        verifica()
        verticeatual = ultimodapilha
        proximo = grafo[f'{verticeatual}'][randint(0,len(grafo[f'{verticeatual}'])-1)] 
        

        if len(grafo[f'{verticeatual}']) == 0:
            rem(verticeatual)
            visitar(pilha[-1])
        elif len(grafo[f'{verticeatual}']) > 0:
            visitados.append(proximo)
            pilha.append(proximo)

            print('prox vertice visitado \n',proximo)
        
            visitar(pilha[-1])
        # elif proximo == []:
              
        

def rem(atual):
        print("vertice popado",pilha.pop())


def verifica():
    if len(pilha)==0 and len(visitados) == len(grafo):
        print("Conexo")
    elif len(pilha)==0 and len(visitados) != len(grafo):
        print("Desconexo")                   

def remove_visitado():
    for k,v in list(grafo.items()):
        print(f'chave {k} = {v}')
        print("atual = ",ultimo) 
        if ultimo in grafo[f'{k}']:
            grafo[f'{k}'].pop(grafo[f'{k}'].index(ultimo))
            print(ultimo)
            print("removido")
        print()    
    print(grafo)


primeiro = input("Digite o vertice inicial: ").upper()
verticeatual = primeiro
visitados.append(verticeatual)
pilha.append(verticeatual)
ultimo=pilha[-1]

visitar(ultimo)
# verticeVisitar = grafo[f'{verticeatual}'][randint(0,len(grafo[f'{verticeatual}'])-1)]
