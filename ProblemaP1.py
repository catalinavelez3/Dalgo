# Catalina Velez 
# 202123930

class SolucionProyecto1:

    def __init__(a, torre):
        a.torre = torre
        a.size = len(torre)
        a.move = 0
        a.inv = [0] * a.size
 
    def legos(a):
        i = 1
        condicion = True
        while i < a.size and i>0:
            if a.torre[i] > a.torre[i-1]:
                condicion1 = True
                condicion2 = True

                if i == a.size -1 :
                    condicion = False

                if i>1:  
                    dif = a.torre[i] - a.torre[i-1]
                    minimo = min(dif, a.torre[i-2] - a.torre[i])

                    if minimo > 0:
                        condicion1 = False
                        condicion2 = False
                        a.torre[i-2] -= minimo
                        a.torre[i-1] += minimo
                        a.inv[i-1] += minimo
                        a.move += minimo

                if i < a.size-1 and condicion2 and condicion:
                    dif = a.torre[i] - a.torre[i-1]
                    ajustes = dif//2 + dif%2 

                    dif2 = a.torre[i] - a.torre[i+1]
                    ajustes1 = dif2//2 

                    if(ajustes >= dif and dif2 > 1 ):
                        dif = min(dif, ajustes1)
                        a.torre[i] -= dif
                        a.torre[i+1] += dif
                        a.inv[i+1] += dif
                        a.move += dif
                        condicion2 = False

                if condicion1 and condicion2 :
                    if a.inv[i]>0:
                        a.move -= 2 
                        a.inv[i] -= 1

                    a.torre[i] -= 1
                    a.torre[i-1] += 1
                    
                    if i > 1:
                        i -= 1
                    a.move += 1 
            else:
                i+=1
            
if __name__ == "__main__":
    with open(r'C:\Users\catal\OneDrive\Documentos\6 SEM\Dalgo\Proyecto1\example.in', 'r') as file:
        casos = int(file.readline().strip())
        for _ in range(casos):
            input_line = file.readline().strip().split(" ")
            size = int(input_line[0])
            torre = list(map(int, input_line[1:]))
            solucion = SolucionProyecto1(torre)
            solucion.legos()
            with open(r'C:\Users\catal\OneDrive\Documentos\6 SEM\Dalgo\Proyecto1\example.out', 'a') as out_file:
                out_file.write(f"Pasos: {solucion.move}, Torre: {solucion.torre}\n")
