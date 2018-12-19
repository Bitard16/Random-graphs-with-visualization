import matplotlib.pyplot as plt
import pylab
import networkx as nx
import random
import time
import math
import numpy as np
import os
import math

#print("Введите данные своего графа, если данные с файла то введите 1 ,  если данные будут введены с руки введите 2, либо 3 если данные заданы в программе")
#ras = int(input())
#if (ras == 1):
 #   f = open('Data','r')
  #  data = f.read()
   # print (data)
#elif (ras == 2):
 #   print ("Введите данные  ")
  #  data = input()
#elif ((ras != 1) and (ras != 2) ):
 #   print ( "Данные заданы в программе"
#def doit (data):
print("Введите число вершин")
number = int(input())
start_time = time.time()
def main():
    i = 0

    while i < number:
        i = i + 1
        if i > 3:
            timeforprog = (time.time() - start_time)
            adj = np.random.randint(0, 2, (i, i))
         # a random directed graph
            G = nx.from_numpy_matrix(adj)  # generator
       # nx.draw(G)  # risuem))
       # plt.show()
            print("Nodes of graph: ")
            print(G.nodes())
            print("Edges of graph: ")
            print(G.edges())
            A = adj
            n = len(G.nodes)
            print(n)
            Visited = [False] * n
            Path = []

            def hamilton(curr):
                Path.append(curr)
                if len(Path) == n:
                    if A[Path[0]][Path[-1]] == 1:
                        return True
                    else:
                        Path.pop()
                        return False
                Visited[curr] = True
                for next in range(n):

                    if A[curr][next] == 1 and not Visited[next]:
                        if hamilton(next):
                            return True
                Visited[curr] = False
                Path.pop()

                return False


            print(hamilton(3))


          #  vremy = ['zero']
           # vershina = [0]
           # vremy.append(timeforprog)
           # vershina.append(n)
           # print(vremy)
          #  print(vershina)
            mainver = str(int(n))
            maintext = str(float(timeforprog))
            print("--- %s seconds ---" % (time.time() - start_time))
            # print(timeforprog)
            f2 = open('DataTime.txt','a')
            f2.write(maintext + os.linesep)
            f2.close()
            f3 = open('DataNodes.txt', 'a')
            f3.write(mainver + os.linesep)
            f3.close()
            f = open('Data.txt', 'a')
            f.write(maintext + '---' + mainver + ' Вершин' + os.linesep)
            f.close()

           

if __name__ == "__main__":
    main()
#g = Graph()
#g.add_edge_list(transpose(adj.nonzero()))

#a = random.randint(1,50) # Генерация случайных целых чисел
#b = random.randint(1,50) # Генерация случайных целых чисел

#def proba(x,y):
  #  if x >y:
      #  return x
    #else:
       # return y
#print(proba(4,5))


#def hamilton(G, size, pt, path=[]):
 #   print('hamilton called with pt={}, path={}'.format(pt, path))
  ###    if len(path)==size:
     #       return path
      #  for pt_next in G.get(pt, []):
       #     res_path = [i for i in path]
        ##   if candidate is not None:  # skip loop or dead end
          #      return candidate
        #print('path {} is a dead end'.format(path))
   # else:
    #    print('pt {} already in path {}'.format(pt, path))

#print("Введите кол-во вершин")
#n = int(input())
#Visited = [False] * n
#Path = []
