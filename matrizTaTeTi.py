#Juego del Gato (Tateti) creado por Mario Pineda
# Matriz 3,3  
# |0,0|0,1|0,2|
# |x
# 1,0|1,1|1,2|
# |2,0|2,1|2,2|
import os
n = [['','',''], ['','',''],['','','']]
mganadores=[ [ [0,0],[0,1],[0,2] ],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],
             [ [0,0],[1,0],[2,0] ],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],
             [ [0,0],[1,1] ,[2,2]],[[0,2],[1,1] ,[2,0]] ]
turnoUno=bool
turnoDos=bool
posvalida=["0,0", "0,1"  , "0,2" , "1,0" , "1,1", "1,2", "2,0", "2,1", "2,2"]
def seleccionsimbolo():
    #seleccion simbolo de cada jugador "X" o "O"
    while True:
        try:
            print("###### Bienvenido al Juego del Gato ######")
            print("Intrucciones")
            print("Se considera una matriz de 3x3 debe seleccionar las coordenadas para indicar su ")
            print("pocisión dentro del tablero, ejemplo para seleccionar la primera casilla ingrese: 0,0 ")
            print("Si selecciona X  comienza jugando ")
            print()
            jugador=input("Para Jugar seleccione su símbolo 'X' o el símbolo 'O'  ").upper()           
            break
        except ValueError :
            print ("Seleccione  el simbolo 'X' o 'O' " )
    return jugador
    
def matrizTablero(matriz):
    cadena = ''
    for i in range(len(matriz)):
        cadena += '|'
        for j in range(len(matriz[i])):
            cadena += '{:>1s}'.format(str(matriz[i][j]))
            cadena += '|'
        cadena += '\n'
    return cadena

 
def Jugador(simbolo,jugador):
    while True:         
            print ("Jugador ", jugador, " su símbolo ", simbolo)          
            posicion=  (input("Ingrese coordenadas de la jugada : "  )).replace(".",",")  
            for val in posvalida:
                if posicion==val: 
                     return posicion                      
    return posicion

def verificatablero(matrizTablero):
#verifica si el tablero esta completo con jugadas
    for r in matrizTablero:
          for c in r:
              if len(c)==0:
                 return True                 
    return False


def turno_0(posicion,simbolo):   
    fila= int(posicion[0])  
    columna=int(posicion[2] )     
    n[fila][columna]=simbolo
    s = matrizTablero(n)
    print(s)

def verificasilla(posicion):
    fila= int(posicion[0])  
    columna=int(posicion[2] ) 
    valor=n[fila][columna]
    if len(valor) == 0:        
        return  True
    else:
        print(matrizTablero(n))
        print ( "####### Casillero Ocupado ######")
        return False
        
def tranforma(tablero,simbolo):
  lista=[] 
  for f in range(3):      
    for c in range(3):          
      if simbolo==tablero[f][c]:         
        lista.append([f,c])     
  return lista

def buscaganador(tab,simbolo): 
    gn=0
    tablero=tranforma(n,simbolo)
    while gn <= len(mganadores):
        listagana=[] 
        for x in range(len(tablero)): 
           # print ("buscando ==>>  ",tablero[x])           
            for c in range(gn,len(mganadores)):       
                #print("en matriz ganadores==>> ",mganadores[c] )
                for i in range(0,3):      
                    if tablero[x]==mganadores[c][i]:                  
                        #print ("Ganador " ,tablero[x])
                        listagana.append(mganadores[c][i])
                break      
        if len(listagana)==3:
            return True         
        gn=gn+1
    return False

def limpiar():
    os.system("cls")
   
def JugarGato():
    limpiar()
    simbolojugador2=""
    simbolojugador1="" 
    if seleccionsimbolo()=="X":   
        simbolojugador2="O"
        simbolojugador1="X"
        turnoUno=True    
    else:
        print ("Comienza Jugando el Jugador 2")
        simbolojugador2="X"
        simbolojugador1="O"
        turnoDos=True
    finjuego=True
    cantjug1=0
    cantjug2=0    
    print (matrizTablero(n))
    ganador=False
    while finjuego==True:     
        if turnoUno==True:
            verifica=False
            while verifica==False:
                posicion=Jugador(simbolojugador1,1)
                verifica= verificasilla(posicion) 
                if verifica==True: 
                    turno_0(posicion,simbolojugador1)                  
            finjuego=verificatablero(n)
            cantjug1=cantjug1+1
            if cantjug1>2:
                ganador=buscaganador(n,simbolojugador1)
                if (ganador):
                    print (" ##### Ganador Jugador 1 #####")
                    break
            if finjuego ==True:
                turnoDos=True
            else:
                turnoDos=False
        if turnoDos==True:
            verifica=False
            while verifica==False:
                posicion=Jugador(simbolojugador2,2)
                verifica=verificasilla(posicion)
                if verifica==True:  
                    turno_0(posicion,simbolojugador2)        
            finjuego=verificatablero(n)   
            cantjug2=cantjug2+1
            if cantjug2>2:
                ganador=buscaganador(n,simbolojugador2)
                if (ganador):
                    print ("#### Ganador Jugador 2 ####")
                    break
            if finjuego==True:
                turnoUno=True   
            else:
                turnoUno=False    
        s = matrizTablero(n)        
        print (s)
    if ganador==False:
        print ("#####  Empate   #####")


JugarGato()
