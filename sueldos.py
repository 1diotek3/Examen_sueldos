
#INDICE 0 = NOMBRE     INDICE 1 = SUELDO

datos = {}

trabajadores = ["Juan Pérez", "María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz", "Elena Fernández"]




def sueldos_a(chambelanes, datos):
    from random import randint as r
    print("e") 
    contador = 0
    
    for trabajador in chambelanes:
        trabajador_sueldo = []
        contador += 1
        sueldo = r(300000,2500000)
        trabajador_sueldo.append(trabajador)
        trabajador_sueldo.append(sueldo)
       
        datos[contador] = trabajador_sueldo
    return datos

def clasificacion_s(diccionario):
    sueldo_a = 0
    sueldo_b = 0
    sueldo_c = 0

    try:
        for trabajador in diccionario:
            
            if diccionario[trabajador][1] < 800000:
                sueldo_a += 1
            elif diccionario[trabajador][1] > 800000 and diccionario[trabajador][1] < 2000000:
                sueldo_b += 1
            elif diccionario[trabajador][1] > 2000000:
                sueldo_c +=1
        print("-"*80)
        print(f"\tSueldos menores a $800.000 \t TOTAL: {sueldo_a} \n")
        print(f"\tNombre de empleado:\t\t Sueldo")
        for trabajador in diccionario:
            if diccionario[trabajador][1] < 800000:
                print(f"\t   {diccionario[trabajador][0]}\t\t\t {diccionario[trabajador][1]}")
        print("\n")
        
        print(f"\tSueldos entre $800.000 a $2.000.000 \t TOTAL: {sueldo_b} \n")
        print(f"\tNombre de empleado:\t\t Sueldo")
        for trabajador in diccionario:
            if diccionario[trabajador][1] > 800000 and diccionario[trabajador][1] < 2000000 :
                print(f"\t   {diccionario[trabajador][0]}\t\t\t {diccionario[trabajador][1]}")

        print("\n")

        print(f"\tSueldos superior a $2.000.000 \t TOTAL: {sueldo_c} \n")
        print(f"\tNombre de empleado:\t\t Sueldo")
        for trabajador in diccionario:
            if diccionario[trabajador][1] > 2000000:
                print(f"\t   {diccionario[trabajador][0]}\t\t\t {diccionario[trabajador][1]}")
        print("\n")
        print("-"*80)
    except Exception as e:
        print(e) 

def estadisticas(diccionario):
   try:
    while True:
        print("-"*80)
        print("seleccione una opcion")
    #profe de puro cuentearme lo haré con lista de mayor a menor y viceversa
        print("1.-Ver sueldo mas alto")
        print("2.- Ver sueldo más bajo")
        print("3.- promedio")
        print("4.- salir")
        op2 = int(input(""))
        match op2:
            case 1:
                lista_ordenada = []
                for key in datos:
                    lista_ordenada.append(datos[key][1])
                    lista_ordenada.sort()
                print("\tSUELDO MÁS ALTO AL MÁS BAJO:")
                print(lista_ordenada)
                for i in range(len(lista_ordenada)):
                    
                    print(f"{i+1}.- {lista_ordenada[9-i]}")
            
            case 2:
                lista_ordenada = []
                for key in datos:
                    lista_ordenada.append(datos[key][1])
                    lista_ordenada.sort()
                print("\tSUELDO MÁS BAJO AL MÁS ALTO:")
                for i in range(len(lista_ordenada)):
                    
                    print(f"{i+1}.- {lista_ordenada[i]}")
            case 3:
                lista_promedio = []
                total = 0
                for key in datos:
                    lista_promedio.append(datos[key][1])
                    
                for sueldo in lista_promedio:
                    total = total + sueldo
                promedio = total / 10
                print(f"El promedio total de el sueldo de todos los trabajadores es ${round(promedio)}")
            case 4:
                print("saliste del submenú")
                break
   except Exception as e:
       print(e)

def liquidaciones(dicionario):
    try:
        ruta = "C:\\Users\\pv-alumno\\Downloads\\EXAMEN\\liquidaciones.csv"
        descuento_salud = 0
        descuento_afp = 0
        sueldo_liquido = 0
        print("-"*80)
        print(f"\t   Nombre empleado \t Sueldo base \t Descuento salud \t Descuento afp Sueldo liquido")
        for key in dicionario:
            for empleado in dicionario[key]:
                descuento_salud = dicionario[key][1] * 0.07
                descuento_afp = dicionario[key][1] * 0.12
                sueldo_liquido = dicionario[key][1] 
                print(sueldo_liquido)
                print(f"Nombre:\t {dicionario[key][0]}\n Sueldo base:\t\t {dicionario[key][1]}\n Descuento salud:\t {descuento_salud}\n Descuento afp:\t\t {descuento_afp}\n Sueldo liquido: \t{sueldo_liquido}\n")
                print("--"*40)
                with open (ruta, "w") as archivo:
                    archivo.write("Nombre,Sueldo base, Descuento salud, Descuento AFP, Sueldo liquido")
                    archivo.write("\n")
                    archivo.write(dicionario[key[0], dicionario[key][1], descuento_salud, descuento_afp, sueldo_liquido])                
                    archivo.writable()
                    archivo.writable
    except Exception as e:
        print(e)


while True:
    print("-"*80)
    print("Bienvenido al menú")
    print("1.-Asignar sueldos aleatorios")
    print("2.- Clasificar sueldos")
    print("3.- Ver estadisticas.")
    print("4.- Reporte de sueldos")
    print("5.- Salir")
    try:
        op = int(input("Seleccione una opcion (1-5)"))
    except ValueError as e:
        print("Ingresa un valor numerico valido")
    match op:
        case 1:
            sueldos_a(trabajadores, datos)
            print(datos)
        case 2:
            clasificacion_s(datos)
        case 3:
            estadisticas(datos)
        case 4:
            liquidaciones(datos)
            
        case 5:
            print("Finalizando programa...")
            print("Desarrollado por Vicente Godoy")
            print("RUT: 22.261.027-3")
            break
        case _:
            print("Ingresa una opcion valida")
           
