print("Bienvenido")

trabajador =(input("ingrese su nombre: "))
sueldo = float(input("ingrese numero de  horas laboradas: "))

if sueldo<=40:
    print(trabajador,"su salario es : ",sueldo*20)
elif sueldo>40:
    print(trabajador,"su salario es ", sueldo*25)
else:
    print("numero de horas incorrecto")