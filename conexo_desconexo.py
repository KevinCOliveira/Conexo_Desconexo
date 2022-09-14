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
    verticeatual = ultimodapilha 
    proximo = grafo[f'{verticeatual}'][randint(0,len(grafo[f'{verticeatual}'])-1)]
    print('prox vertice visitado',proximo)

def remove_visitado():
    for k,v in list(grafo.items()):
        print(f'chave {k} = {v}')

        if verticeVisitar in grafo[f'{k}']:
            grafo[f'{k}'].pop(grafo[f'{k}'].index(verticeVisitar))
            print(verticeVisitar)
            print("removido")
            print(grafo)    

primeiro = input("Digite o vertice inicial: ").upper()
verticeatual = primeiro
visitados.append(verticeatual)
verticeVisitar = grafo[f'{verticeatual}'][randint(0,len(grafo[f'{verticeatual}'])-1)]

def add_rem():
    for k in list(grafo.items()):
        while (len(grafo[f'{k}'])) > 0:
            visitados.append(verticeVisitar)
            pilha.append(verticeVisitar)
        pilha.pop(k)   
        visitar(pilha[-1])

#     if len(visitados) == len(grafo):
#         break
# print(visitados)
# print(grafo) 


#lkjafhaklf

print("teste")