import csv
import random
import statistics as stat

def asignar_sueldos(trabajadores):
    listaTrabajadores={}
    listaTrabajadores={trabajador : random.randint(300000,2500000) for trabajador in trabajadores}
    print("\nAsignación de sueldos finalizada corectamente.\n")
    return listaTrabajadores

def clasificar_Sueldos(listaTrabajadores):
    cantidadMenores=0
    cantidadMedios=0
    cantidadMayores=0
    sueldosMenores={}
    sueldosMedios={}
    sueldosMayores={}
    listaSueldos=list(listaTrabajadores.values())
    for sueldo in listaSueldos:
        if sueldo<800000:
            cantidadMenores+=1
    print("\nSueldos menores a $800.000\nTotales: ",cantidadMenores)
    for trabajador,sueldo in listaTrabajadores.items():
        if sueldo<800000:
            print(trabajador, ": $", sueldo)


    for sueldo in listaSueldos:
        if sueldo>=800000 and sueldo<=2000000:
            cantidadMedios+=1
    print("\nSueldos entre $800.000 y $2.000.000\nTotales: ",cantidadMedios)
    for trabajador,sueldo in listaTrabajadores.items():
        if sueldo>=800000 and sueldo<=2000000:
            print(trabajador," $",sueldo)

    for sueldo in listaSueldos:
        if sueldo>2000000:
            cantidadMayores+=1
    print("\nSueldos mayores a $2.000.000\nTotales: ",cantidadMayores)
    for trabajador,sueldo in listaTrabajadores.items():
        if sueldo>2000000:
            print(trabajador," $",sueldo)

    print("\nTotal sueldos: ",sum(listaSueldos))

            

def estadisticas_Sueldos(listaTrabajadores):
    listaSueldos=list(listaTrabajadores.values())
    maximo=max(listaSueldos)
    minimo=min(listaSueldos)
    promedio=int(sum(listaSueldos)/len(listaSueldos))
    mediaGeo=int(stat.geometric_mean(listaSueldos))
    return maximo,minimo,promedio,mediaGeo

def reporte_Sueldos(listaTrabajadores):
    print("Nombre empleado / Sueldo base / Descuento Salud / Descuento Afp / Sueldo Líquido")

    for trabajador,sueldo in listaTrabajadores.items():
        sueldoBase=sueldo
        descuentoSalud=int(sueldo*0.07)
        descuentoAFP=int(sueldo*0.12)
        sueldoLiq=sueldoBase-descuentoAFP-descuentoSalud
        print(trabajador," / ",sueldoBase," / ",descuentoSalud," / ",descuentoAFP," / ",sueldoLiq)
    
    with open("reporte_de_sueldos.csv","w") as archivo:
        escritor=csv.writer(archivo)
        escritor.writerow(["Nombre Empleado","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Liquido"])
        for trabajador,sueldo in listaTrabajadores.items():
            sueldoBase=sueldo
            descuentoSalud=int(sueldo*0.07)
            descuentoAFP=int(sueldo*0.12)
            sueldoLiq=sueldoBase-descuentoAFP-descuentoSalud
            escritor.writerow([trabajador,sueldoBase,descuentoSalud,descuentoAFP,sueldoLiq])