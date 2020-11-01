# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.pyplot as plt
import random
import numpy as np
#plt.rcParams['figure.figsize'] = (16, 9)
#plt.style.use('ggplot')

# PARÁMETROS
cant_pi = 50 # Cantidad población inicial = 50
cant_corridas = 1500 # Cantidad de corridas
pc = 0.75 # Probabilidad de crossover  
pm = 0.25 # Probabilidad de mutación
cant_molinos = 30 # Cantidad de molinos
u0 = 5 # Velocidad del viento en m/s
coef_arrastre = 0.05 # alpha
coef_induccionAxial = 0.333 # a
diam_turbina = 47 # Metros
tam_celda = 94 # Metros
cant_celdas = 100 # Cantidad de celdas en el terreno 10x10
r = 6 # Elitismo

# PARÁMETROS CALCULADOS
radio_estela = 2 * diam_turbina/2 # El coeficiente puede ser entre 1 y 4
long_estela = 9 * diam_turbina # El coeficiente puede ser entre 6 y 18

# FUNCION DE POTENCIA GENERADA
# Argumento: velocidad del viento (Double)
# Devuelve: potencia generada (Entero)
def potencia_generada(ux):
    x=int(ux) # Parte entera
    if x<=4: p=0
    if x==5: p=53
    if x==6: p=106
    if x==7: p=166
    if x==8: p=252
    if x==9: p=350
    if x==10: p=464
    if x==11: p=560
    if x==12: p=630
    if x>=13 and x<=25: p=660
    if x>25: p=0
    return p

# FUNCION OBJETIVO
# Argumento: Posiciones de los molinos en el parque (Array[10x10] de Enteros)
# Devuelve: 1: Potencia total del parque (Entero)
#           2: Potencia generada por cada molino (Array[10x10] de Enteros)
def funcion_objetivo(matriz): 
    total_pot = 0
    matriz_pot = []
    for j in range(10): # Recorro por columna
        pos_molino_ant = -10 # El primer molino con el que comparo está muy lejos
        col_pot = [] 
        for i in range(10): # Recorro cada elemento de la columna
            if matriz[i][j] == 1: # Si detecto un molino, tengo que saber cuanto genera
                x = (i-pos_molino_ant)*96 # Distancia del molino respecto al anterior
                pos_molino_ant = i # Guardo la posicion del molino
                if x < long_estela: # Si está dentro de la estela, recibe un viento menor
                    ux = u0*(1-(2*coef_induccionAxial/((1+coef_arrastre*(x/radio_estela))**2))) 
                else: # Si no, el viento incide directo
                    ux = u0
                p = potencia_generada(ux) # Con ese viento, genera 'p' kw  
                col_pot.append(p) # Pongo la potencia en el lugar del molino
                total_pot += p # Acumulo para calcular la potencia total
            else: # Si no, pongo un cero en donde no hay un molino
                col_pot.append(0)
        col=np.array(col_pot) # List a Array
        matriz_pot.append(col) # Agrego la columna
    mat=np.array(matriz_pot) # List a Array
    mat=np.transpose(mat) # Transpuesta
    return total_pot, mat

# POBLACION INICIAL
# Argumento: Null
# Devuelve: Población de 50 parque eólicos, cada uno tiene la ubicacion de los 25 molinos. (List[50] de Array[10x10] de Enteros)
def crear_poblacion_inicial():
    pob = []
    for _ in range(cant_pi):
        molinos = random.randrange(cant_molinos)
        data = [1]*molinos + [0]*(100-molinos) # Creo lista con tantos 1 como cantidad de molinos haya en el individuo.
        random.shuffle(data) # Mezclo la Lista
        dataArray = np.array(data) # Paso Lista a Array
        matriz = np.reshape(dataArray,(10,10)) # Le doy forma de Matriz de 10x10
        pob.append(matriz) # Agrego individuo a la población
    return pob

# POTENCIA DE CADA FILA Y CADA COLUMNA
# Argumento: Posiciones de los molinos en el parque. (Array[10x10] de Enteros)
# Devuelve: 1: Potencia de cada fila. (List[10] de Enteros)
#           2: Potencia de cada columna. (List[10] de Enteros)
def potencias_fila_columna(matriz):
    _, matriz_pot = funcion_objetivo(matriz) # No uso el primer return
    fila = []
    col = []
    for i in range(10): # Cada fila i
        f = 0
        for j in range(10): # Cada elemento j de la fila
            f += matriz_pot[i][j] # Acumulo la potencia cada molino de la fila i
        fila.append(f)
    for j in range(10): # Cada columna j
        c = 0
        for i in range(10): # Cada elemento i de la columna
            c += matriz_pot[i][j] # Acumulo la potencia cada molino de la columna j
        col.append(c)   
    return fila,col

# CROSSOVER: Comparar y quedarse con la mejor fila o columna para cada posición.
# Argumento: 2 padres, que son posiciones de los molinos en el parque. (Array[10x10] de Enteros)
# Devuelve: 2 hijos, que son posiciones de los molinos en el parque. (Array[10x10] de Enteros)
def crossover(matriz1,matriz2):
    if random.random()<=pc:
        m1_f, m1_c = potencias_fila_columna(matriz1) # Obtengo potencias por filas y por columnas de Padre 1
        m2_f, m2_c = potencias_fila_columna(matriz2) # Obtengo potencias por filas y por columnas de Padre 2

        matriz_fila = np.empty((0,10), int) # Array vacío para hacer el stack
        matriz_col = np.empty((0,10), int) # Array vacío para hacer el stack
        # Hijo 1
        for i in range(10):
            if m1_f[i]>m2_f[i]: # Si la fila i del Padre 1 genera más potencia que la fila i del Padre 2:
                matriz_fila = np.vstack((matriz_fila, matriz1[i])) # Uso fila i de Padre 1 para crear la fila i del Hijo 1
            else: # Si la fila i del Padre 2 genera más potencia que la fila i del Padre 1:
                matriz_fila = np.vstack((matriz_fila, matriz2[i])) # Uso fila i de Padre 2 para crear la fila i del Hijo 1
        # Hijo 2
        for i in range(10): 
            if m1_c[i]>m2_c[i]: # Si la columna i del Padre 1 genera más potencia que la columna i del Padre 2:
                matriz_col = np.vstack((matriz_col, matriz1[:,i])) # Uso columna i de Padre 1 para crear la columna i del Hijo 2
            else: # Si la columna i del Padre 2 genera más potencia que la columna i del Padre 1:
                matriz_col = np.vstack((matriz_col, matriz2[:,i])) # Uso columna i de Padre 2 para crear la columna i del Hijo 2
        matriz_col = matriz_col.transpose() # Transpuesta, porque usé stack vertical
    else:
        matriz_fila = matriz1
        matriz_col = matriz2
    return matriz_fila, matriz_col

# MUTACION 1
# Argumento: Posiciones de los molinos en el parque. (Array[10x10] de Enteros)
# Devuelve: Posiciones de los molinos en el parque. (Array[10x10] de Enteros)
def mutacion(matriz):
    if random.random()<=pm:
        f = random.randrange(10) # Elijo una fila
        c = random.randrange(10) # Elijo una columna
        if matriz[f,c] == 0: 
            matriz[f,c] = 1 # Cambio el bit
        else:
            matriz[f,c] = 0 # Cambio el bit
    return matriz

# MUTACION 2
# Argumento: Posiciones de los molinos en el parque. (Array[10x10] de Enteros)
# Devuelve: Posiciones de los molinos en el parque. (Array[10x10] de Enteros)
def mutacion2(matriz):
    if random.random()<=pm:
        listaOcupados = []
        listaVacios = []
        for i in range(10):
            for j in range(10):
                if matriz[i][j]==0:
                    listaVacios.append((i,j))
                else:
                    listaOcupados.append((i,j))
        coordenadaOcupada = random.choice(listaOcupados)
        coordenadaVacia = random.choice(listaVacios)
        matriz[coordenadaOcupada[0],coordenadaOcupada[1]] = 0
        matriz[coordenadaVacia[0],coordenadaVacia[1]] = 1
    return matriz


# RECORTE: Elimina molinos que superen el máximo permitido por parque. Elimina los que menos generan.
# Argumento: Posiciones de los molinos en el parque. (Array[10x10] de Enteros)
# Devuelve: Posiciones de los molinos en el parque. (Array[10x10] de Enteros)
def recorte(matriz):
    x = np.sum(matriz) # Cantidad de molinos
    _, matriz_pot = funcion_objetivo(matriz) # Potencia generada por cada molino
    for i in range(10):
        for j in range(10):
            if matriz_pot[i][j]==0 and matriz[i][j] == 1:
                matriz[i][j]=0
    if x > cant_molinos: # Si supera los permitidos
        # Cambiar los ceros por 99999. Permite buscar los que menos generan, sin que los ceros influyan. Mejorar!
        for i in range(10):
            for j in range(10):
                if matriz_pot[i][j]==0 and matriz[i][j] == 0:
                    matriz_pot[i][j]=99999

        for _ in range(x-cant_molinos): # Repite la cantidad de molinos excedentes
            coordenadas = np.where(matriz_pot == np.amin(matriz_pot)) # Índices de los mínimos elementos. 
            # 'Where' devuelve en formato "(array([4, 6], dtype=int32), array([3, 7], dtype=int32))" si hay dos mínimos y están en (4,3) y (6,7)
            f = coordenadas[0][0] # Fila del primer mínimo
            c = coordenadas[1][0] # Columna del primer mínimo
            matriz[f,c] = 0 # Borro el molino de la posición donde está el mínimo
            matriz_pot[f,c] = 99999 # Para que no lo vuelva a detectar como mínimo
    return matriz

# RULETA: Se llena una ruleta según los fitness de cada individuo y se realizan 50 tiradas
# Argumento: Poblacion de parques eólicos (List[50] de Array 10x10 de Enteros)
# Devuelve: 50 tiradas a la Ruleta (List[50] de Enteros)
def tirar_ruleta(poblacion):
    # RUTINA PARA LLENAR RULETA
    cant_casilleros = 100 # 100% de la ruleta
    ruleta = [] # Casilleros
    tirada = [] # Resultados
    pos_fin = 0 # Auxiliar para completar ruleta
    fitness = funcion_fitness(poblacion) # Calculo fitness de cada individuo
    for i in range(len(poblacion)):
        cant_casilleros_i = round(fitness[i]*cant_casilleros) # Porcentaje de casilleros con respecto a 100
        #Lleno la ruleta con la posición del cromosoma
        for _ in range(pos_fin,pos_fin+cant_casilleros_i):
            ruleta.append(i)
        pos_fin += cant_casilleros_i
    
    # RUTINA PARA SACAR 50 NUMEROS
    for i in range(len(poblacion)):
        #Saco un random de la ruleta
        num = random.randrange(len(ruleta))
        tirada.append(ruleta[num])
    return tirada

# FITNESS
# Argumento: Población de parques. (List[50] de Array[10x10] de Enteros)
# Devuelve: Fitness de cada parque. (List[50] de Enteros)
def funcion_fitness(poblacion):
    suma_fo = 0 # Acumulado
    potencias = [] # Lista de potencias de cada individuo
    fitness = [] # Lista de fitness de cada individuo
    for i in range(len(poblacion)):
        pot, _ = funcion_objetivo(poblacion[i])
        potencias.append(pot)
        suma_fo += pot
    for i in range(len(poblacion)):
        fitness.append(potencias[i]/suma_fo)
    return fitness

# COMPUTAR: Obtiene valores característicos de la población generada por una corrida
# Argumento: Poblacion (List[50] de Array[10x10] de Enteros)
# Devuelve: Mínimo, máximo, promedio e indice de elemento que genera el máximo, de toda una poblacion. (Tupla[4] de Double)
def computar(pob):
    potencias = []
    for i in range(len(pob)):
        p,_ = funcion_objetivo(pob[i]) # Potencia del parque eólico i
        potencias.append(p) # Lista de potencias
    maxi = max(potencias) # Máximo de la lista
    mini = min(potencias) # Mínimo de la lista
    prom = sum(potencias)/len(potencias) # Promedio de la lista
    indi = potencias.index(maxi) # Indice donde se da el máximo en la población.
    return mini,maxi,prom,indi

# GRAFICAR RESULTADOS
# Argumento: Tabla = Lista de tuplas. Cada tupla es una fila de la tabla y tiene (minimo,maximo,promedio,indice). (Lista[1500] de Tupla[4] de Double)
# Devuelve: Null
def graficar_resultados(data):
    plt.title('Grafica')
    lista_minimos = []
    lista_maximos = []
    lista_promedios = []
    for d in data:
        lista_minimos.append(d[0])
        lista_maximos.append(d[1])
        lista_promedios.append(d[2])
    print(max(lista_maximos))
    plt.plot(lista_minimos,'ro-',markersize=0.5,lw=0.5,color='red',label="Mínimos")
    plt.plot(lista_maximos,'ro-',markersize=0.5,lw=0.5,color='blue',label="Máximos")
    plt.plot(lista_promedios,'ro-',markersize=0.5,lw=0.5,color='green',label="Promedios")
    plt.grid(True)
    plt.xlabel('Número de corrida')
    plt.ylabel('Valor función objetivo')
    plt.ylim(bottom=0)
    plt.legend()
    plt.show()
    #return

# GRAFICAR PARQUE EÓLICO
# Argumento: Posiciones de los molinos en el parque. (Array[10x10] de Enteros)
# Devuelve: Null
def graficar_parque(matriz):
    cmap = mpl.colors.ListedColormap(['white','black']) # Colores a utilizar: blanco y negro
    img = plt.imshow(matriz, interpolation = 'nearest', cmap = cmap) # Dibujar matriz
    plt.grid(False) # Saco rejilla
    plt.show(img)
    return

# REPORTE: usado para mostrar funcionamiento del programa
# Argumento: 2 parques eólicos. (Array[10x10] de Enteros)
def reporte(matriz1,matriz2):
    m1_f, m1_c = potencias_fila_columna(matriz1) # Obtengo potencias por filas y por columnas de Padre 1
    m2_f, m2_c = potencias_fila_columna(matriz2) # Obtengo potencias por filas y por columnas de Padre 2
    
    m1_c = np.array(m1_c)
    m2_c = np.array(m2_c)

    cant1 = np.sum(matriz1)
    cant2 = np.sum(matriz2)

    p1, matriz1 = funcion_objetivo(matriz1)
    p2, matriz2 = funcion_objetivo(matriz2)

    m1_f = np.array(m1_f+[p1]).reshape((11, 1))
    m2_f = np.array(m2_f+[p2]).reshape((11, 1))

    matriz1 = np.vstack((matriz1, m1_c)) # Agrega una fila con las potencias de cada columna
    matriz1 = np.hstack((matriz1, m1_f)) # Agrega un columna con las potencias de cada fila

    matriz2 = np.vstack((matriz2, m2_c)) # Agrega una fila con las potencias de cada columna
    matriz2 = np.hstack((matriz2, m2_f)) # Agrega un columna con las potencias de cada fila

    print('Parque 1:', cant1, 'molinos')
    print(matriz1)
    print('Parque 2:', cant2, 'molinos')
    print(matriz2)

# PROGRAMA MUESTRA: usado para mostrar funcionamiento del programa
def programa_muestra():
    global cant_pi
    global cant_corridas
    global pm
    global pc
    cant_pi = 2
    cant_corridas = 2
    pm = 1
    pc = 1
    pob = crear_poblacion_inicial() # POBLACION INICIAL
    print('1 - SELECCION *************************************')
    a = pob[0] # SELECCIONAR PADRE 1
    b = pob[1] # SELECCIONAR PADRE 2
    reporte(a,b)
    print('2 - CROSSOVER *************************************')
    c,d = crossover(a,b) # CRUZAR PADRE 1 CON PADRE 2
    reporte(c,d)
    print('3 - RECORTE *************************************')
    c = recorte(c)  # RECORTAR HIJO 1
    d = recorte(d)  # RECORTAR HIJO 2
    reporte(c,d)
    print('4 - MUTACION *************************************')
    c = mutacion2(c) # MUTAR HIJO 1
    d = mutacion2(d) # MUTAR HIJO 2
    reporte(c,d)


# ELITISMO
def elitismo(poblacion):
    elite = []
    lista_fitness = []
    fitness = funcion_fitness(poblacion)
    for i in range(len(poblacion)):
        lista_fitness.append([poblacion[i],fitness[i]])
    lista_fitness.sort(key=lambda x:x[1], reverse=True)
    for i in range(r):
        elite.append(lista_fitness[i][0])
    return elite


# PROGRAMA PRINCIPAL
def programa_principal():
    pob = crear_poblacion_inicial() # POBLACION INICIAL
    tabla = []
    max_potencia = 0
    max_matriz = []
    #max_matriz = np.empty((0,10), int)
    #tabla.append(computar(pob))
    for j in range(cant_corridas):
        pobHijos = elitismo(pob)
        ruleta = tirar_ruleta(pob) # RULETA
        for i in range(int((cant_pi-r)/2)): # Voy a hacer [(poblacionInicial - r)/2] cruces
            a = pob[ruleta[2*i]]     # SELECCIONAR PADRE 1
            b = pob[ruleta[(2*i)+1]] # SELECCIONAR PADRE 2
            c,d = crossover(a,b) # CRUZAR PADRE 1 CON PADRE 2
            c = mutacion(c) # MUTAR HIJO 1
            d = mutacion(d) # MUTAR HIJO 2
            c = recorte(c)  # RECORTAR HIJO 1
            d = recorte(d)  # RECORTAR HIJO 2
            pobHijos.append(c) # INSERTAR HIJO 1
            pobHijos.append(d) # INSERTAR HIJO 2
            
        fila = computar(pobHijos) # COMPUTAR POBLACION: mini,maxi,prom,indi
        if fila[1] > max_potencia:
            print("Entra en: ",j)
            max_potencia = fila[1] # Guardar máxima potencia
            max_matriz = pobHijos[fila[3]] # Guardar mejor parque
            print(max_matriz)
            print(max_potencia)
            #reporte(max_matriz,max_matriz)
        tabla.append(fila) # Rellenar tabla
        pob = pobHijos
        #print(j,"pot: ",max_potencia)
        #reporte(max_matriz,max_matriz)
    #graficar_resultados(tabla) # GRAFICAR CORRIDAS
    print("fin")
    print(max_matriz)
    #print(funcion_objetivo(max_matriz))
    reporte(max_matriz,max_matriz)
    graficar_parque(max_matriz) # GRAFICAR PARQUE EÓLICO
    

programa_principal()
#programa_muestra()