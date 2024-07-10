import statistics
import random
import csv
import funciones as fn

trabajadores = [
    "Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"
    ]
listaTrabajadores={}

#Menu:

while True:
    print("-----MENÚ-----")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadisticas")
    print("4. Reporte de sueldos")
    print("5. Salir del progama")
    opcion=int(input("\nPor favor elija una opción: "))

    if opcion==1:
        listaTrabajadores=fn.asignar_sueldos(trabajadores)
    
    elif opcion==2:
        fn.clasificar_Sueldos(listaTrabajadores)

    elif opcion==3:
        maximo,minimo,promedio,mediaGeo=fn.estadisticas_Sueldos(listaTrabajadores)
        print("\nEl Sueldo máximo es: ", maximo,"\nEl sueldo mínimo es: ",minimo,"\nEl promedio de los sueldos es de: ",promedio,"\nLa media geometrica es de: ",mediaGeo,"\n")

    elif opcion==4:
        fn.reporte_Sueldos(listaTrabajadores)

    elif opcion==5:
        print("\nFinalizando programa...\nDesarrollado por Cristián Collao\nRUT: 19.450.543-4\n")
        break
    else:
        print("\nOpción inválida, por favor seleccione un número entre 1 y 5")