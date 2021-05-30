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
        
    def entradaVertices(self):
        self.entrada = tk.Entry(self)
        self.entrada.pack(side="top")
        self.v = tk.StringVar()
        self.entrada["textvariable"] = self.v
    
    def entradaAristas(self):
        self.entrada1 = tk.Entry(self)
        self.entrada1.pack(side="top")
        self.e = tk.StringVar()
        self.entrada1["textvariable"] = self.e

    def dibujarGrafo(self):
        self.botton= tk.Button(self)
        self.botton["text"] = "Dibujar Grafo"
        self.botton["command"] = self.f_dibujar
        self.botton.pack(side="left")

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

        nx.draw(G, with_labels=True)
        plt.show()

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

        for i in range(len(self.vertice)):
            for j in range(len(self.vertice)):
                print(self.matriz[i][j], end=''+" ")
            print()

root = tk.Tk()
app = Application(master=root)
app.master.title("Proyecto de Teoria: Grafos")
#app.master.maxsize(1000,500)
app.mainloop()
