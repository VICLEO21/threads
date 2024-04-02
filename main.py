from lib import *
import threading
import time

### Ejercicio introducción inicio
#def tiempo ():
#    print ("Haciendo tiempo...")
#    time.sleep(1) #se queda esperando n segundos
#    print ("Tiempo hecho")
#tiempo()

#t0 = time.time()
#listaHilos = []
#for i in range (4):
#    t =  threading.Thread (target=tiempo)
#    listaHilos.append (t)
#    t.start ()

#for t in listaHilos:
#    t.join() ###Join para que se junte al programa y no de quede volando nuestro hilo

#TiempoFinal = time.time() - t0
#print (f'Tiempo total de ejecución: {TiempoFinal}')
### Ejercicio introducción final


print(f'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

print ("Hilo principal o 1 hilo")
print ("")

def contador (inicio,fin):
    arrayNum = []
    for i in range (inicio, fin+1, 1):
        arrayNum.append (i)
        time.sleep (0.02)
    return arrayNum

t0 = time.time ()
listaNumeros = contador(1,100)
TiempoFinal = time.time() - t0
print (f'Tiempo total de ejecución: {TiempoFinal}')
print (listaNumeros)

print(f'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

print ("Usando 2 hilos")
print ("") 

globalArrayNum = []
def contador2hilos (inicio,fin):
    for i in range (inicio, fin+1, 1):
        globalArrayNum.append (i)
        time.sleep (0.02)
    return globalArrayNum

t0 = time.time ()
listaHilos = []

t = threading.Thread(target=contador2hilos, args=(1,50))
listaHilos.append(t)
t.start ()

t = threading.Thread(target=contador2hilos, args=(51,100))
listaHilos.append(t)
t.start ()

for t in listaHilos:
    t.join()

TiempoFinal = time.time() - t0
print (f'Tiempo total de ejecución: {TiempoFinal}')
globalArrayNum.sort()
print (globalArrayNum)

print(f'---------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

print ("Usando 4 hilos")
print ("") 


globalArrayNum = []
def contador4hilos (inicio,fin):
    for i in range (inicio, fin+1, 1):
        globalArrayNum.append (i)
        time.sleep (0.02)
    return globalArrayNum

t0 = time.time ()
listaHilos = []

for i in range (4):
    t =  threading.Thread (target=contador4hilos, args=(1,100//4))
    listaHilos.append (t)
    t.start ()

#t = threading.Thread(target=contador4hilos, args=(1,24))
#listaHilos.append(t)
#t.start ()

#t = threading.Thread(target=contador4hilos, args=(25,49))
#listaHilos.append(t)
#t.start ()

#t = threading.Thread(target=contador4hilos, args=(50,74))
#listaHilos.append(t)
#t.start ()

#t = threading.Thread(target=contador4hilos, args=(75,100))
#listaHilos.append(t)
#t.start ()

for t in listaHilos:
    t.join()

TiempoFinal = time.time() - t0
print (f'Tiempo total de ejecución: {TiempoFinal}')
globalArrayNum.sort()
print (globalArrayNum)