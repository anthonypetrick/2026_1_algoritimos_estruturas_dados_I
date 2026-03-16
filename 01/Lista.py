from No import No

class Lista:

    def __init__(self):
        self.inicio = None

    def add(self, valor)
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
        else:
            if nodo.dado < self.inicio:
                nodo.proximo = self.inicio
                self.inicio = nodo
            else:
                ant = self.inicio
                aux = self.inicio.prox

                while aux :
                    if nodo.dado < aux.dado
                        nodo.prox = aux
                        ant.prox = nodo
                        break
                    else:
                        ant = aux
                        aux = aux.prox
                if aux == None:
                    ant.prox = nodo
        self.imprimir()


    def print(self):
        print("\nLista Encadeada")
        if self.inicio = None
            print("\nLista Vazia")
        aux = self.inicio
        while aux :
            print("\n" + aux.dado)
            aux = aux.prox
