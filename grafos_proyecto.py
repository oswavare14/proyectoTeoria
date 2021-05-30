import tkinter as tk
import matplotlib.pyplot as plt
import networkx as nx

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.entradaVertices()
        self.entradaAristas()
        self.dibujarGrafo()
        self.gradoGrafo()
        self.gradoMenor()
        self.gradoMayor()
        self.ciclos()
        self.entradaCamino()

    def entradaVertices(self):
        self.text=tk.Label(self)
        self.text["text"]= "Vertices"
        self.text.pack(side="top")

        self.entrada = tk.Entry(self)
        self.entrada.pack(side="top")
        self.v = tk.StringVar()
        self.entrada["textvariable"] = self.v
    
    def entradaAristas(self):
        self.text=tk.Label(self)
        self.text["text"]="Aristas"
        self.text.pack(side="top")

        self.entrada1 = tk.Entry(self)
        self.entrada1.pack(side="top")
        self.e = tk.StringVar()
        self.entrada1["textvariable"] = self.e

    def dibujarGrafo(self):
        self.botton= tk.Button(self)
        self.botton["text"] = "Dibujar Grafo"
        self.botton["command"] = self.f_dibujar
        self.botton.pack(side="top")

    def gradoGrafo(self):
        self.boton=tk.Button(self)
        self.boton["text"]="Grado del Grafo"
        self.boton["command"] = self.f_gradoGrafo
        self.boton.pack(side="top")

    def gradoMenor(self):
        self.boton=tk.Button(self)
        self.boton["text"]="Grado menor"
        self.boton["command"] = self.f_gradoMenor
        self.boton.pack(side="top")

    def gradoMayor(self):
        self.boton=tk.Button(self)
        self.boton["text"]="Grado mayor"
        self.boton["command"] = self.f_gradoMayor
        self.boton.pack(side="top")
    
    def ciclos(self):
        self.boton=tk.Button(self)
        self.boton["text"]="Ciclos"
        self.boton["command"] = self.f_ciclos
        self.boton.pack(side="top")

    def entradaCamino(self):
        self.text=tk.Label(self)
        self.text["text"]= "Camino"
        self.text.pack(side="top")

        self.entrada = tk.Entry(self)
        self.entrada.pack(side="top")
        self.cam = tk.StringVar()
        self.entrada["textvariable"] = self.cam

        self.botton= tk.Button(self)
        self.botton["text"] = "Buscar el camino"
        self.botton["command"] = self.f_camino
        self.botton.pack(side="top")
 

    def f_ciclos(self):
        self.arista = self.e.get().replace(')','')
        self.arista = self.arista.replace('(','').split(sep=" ")

        self.aristas = []

        for i in self.arista:
            self.temp = []
            self.temp.append(int(i[0]))
            self.temp.append(int(i[2]))
            self.aristas.append(self.temp)

        G = nx.DiGraph(self.aristas)
        self.string = ""

        if len(list(nx.simple_cycles(G))) == 0:
            string="No hay ciclos"
        else:
            string="Si hay ciclos"

        self.text=tk.Label(self)
        self.text["text"]= string
        self.text.pack(side="bottom")


    def f_gradoMayor(self):
        self.m = self.f_matrix()
        self.pos = 0
        self.acum = 0
        self.cont = 0

        for i in self.m:
            self.temp = 0
            for j in i:
                if j == "1":
                    self.temp += 1

            if self.temp > self.acum:
                self.pos = self.cont + 1
                self.acum = self.temp
            self.cont += 1

        string = "El vertice con mayor grado: " + str(self.pos)

        self.text=tk.Label(self)
        self.text["text"]= string
        self.text.pack(side="bottom") 

    def f_gradoMenor(self):
        self.m = self.f_matrix()
        self.pos = 0
        self.acum = 1000
        self.cont = 0

        for i in self.m:
            self.temp = 0
            for j in i:
                if j == "1":
                    self.temp += 1

            if self.temp <= self.acum:
                self.pos = self.cont + 1
                self.acum = self.temp
            self.cont += 1

        string = "El vertice con menor grado: " + str(self.pos)

        self.text=tk.Label(self)
        self.text["text"]= string
        self.text.pack(side="bottom")



    def f_gradoGrafo(self):
        self.m = self.f_matrix()
        self.cont = 0

        for i in self.m:
            for j in i:
                if j == "1":
                    self.cont += 1
        string = "El grado del grafo es de: " + str(self.cont)

        self.text=tk.Label(self)
        self.text["text"]= string
        self.text.pack(side="bottom")

    def f_dibujar(self):
        self.vertice = self.v.get().split(sep=",")
        
        self.arista = self.e.get().replace(')','')
        self.arista = self.arista.replace('(','').split(sep=" ")

        self.aristas = []

        for i in self.arista:
            self.temp = []
            self.temp.append(i[0])
            self.temp.append(i[2])
            self.aristas.append(self.temp)

        G = nx.Graph()
        G.add_nodes_from(self.vertice)

        for i in self.aristas:
            G.add_edge(i[0],i[1])

        self.f_printMatriz()

        nx.draw(G,node_color="g",with_labels=True,font_color="w")
        plt.show()

    def f_camino(self):
        self.cami = self.cam.get().split(sep=" ")
        self.vertice = self.v.get().split(sep=",")
        
        self.arista = self.e.get().replace(')','')
        self.arista = self.arista.replace('(','').split(sep=" ")

        self.aristas = []
        self.vertices = []
        self.camin = []

        for i in self.cami:
            self.camin.append(int(i))

        for i in self.vertice:
            self.vertices.append(int(i))

        for i in self.arista:
            self.temp = []
            self.temp.append(int(i[0]))
            self.temp.append(int(i[2]))
            self.aristas.append(self.temp)

        G = nx.Graph()
        G.add_nodes_from(self.vertices)

        for i in self.aristas:
            G.add_edge(i[0],i[1])
        
        self.pa = []
        for path in nx.all_simple_paths(G, source=self.camin[0], target=self.camin[1]):
            self.pa.append(path)
            print(path)
        print()

        self.corto = 1000
        for i in self.pa:
            if len(i) < self.corto:
                self.corto = len(i)
                self.camCorto = i
        
        K = nx.Graph()
        K.add_nodes_from(self.camCorto)

        for i in range(len(self.camCorto)-1):
            if i == len(self.camCorto):
                break
            else:
                K.add_edge(self.camCorto[i], self.camCorto[i+1])

        nx.draw(K,node_color="g",with_labels=True,font_color="w")
        plt.show()
        

    def f_printMatriz(self):
        self.m = self.f_matrix()

        for i in range(len(self.m)):
            for j in range(len(self.m)):
                print(self.m[i][j], end=''+" ")
            print()
        print()


    def f_matrix(self):
        self.vertice = self.v.get().split(sep=",")
        self.arista = self.e.get().split(sep=" ")
        self.revArista = []

        for i in self.arista:
            self.temp = []
            self.temp.append(i[4])
            self.temp.append(i[3])
            self.temp.append(i[2])
            self.temp.append(i[1])
            self.temp.append(i[0])
            self.revArista.append(self.temp)


        self.matriz = []

        for i in range(len(self.vertice)):
            self.row = []
            for j in range(len(self.vertice)):
                self.row.append("0")

            for k in self.arista:
                if int(k[1])-1 == i:
                    pos = int(k[3]) - 1
                    self.row.pop(pos)
                    self.row.insert(pos,"1")

            for t in self.revArista:
                if int(t[1])-1 == i:
                    pos = int(t[3]) - 1
                    self.row.pop(pos)
                    self.row.insert(pos,"1")

            for n in range(len(self.vertice)):
                if i == n:
                    self.row.pop(i)
                    self.row.insert(i,"-")
        
            self.matriz.append(self.row)

        return(self.matriz)

root = tk.Tk()
app = Application(master=root)
app.master.title("Proyecto de Teoria: Grafos")
#app.master.maxsize(1000,500)
app.mainloop()
