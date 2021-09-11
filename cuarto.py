print("Bienvenido")

salario=float(input("ingrese su salario "))


if salario > 2000:
    print("su aumento es de 5'%' y su aumento es ", salario*0.05, "y su nuevo salario es", (salario*0.05)+salario) 
elif salario <= 2000:
    print("Su aumento es de 10'%' y su aumento es  ",salario*0.10, "y su nuevo salario es", (salario*0.10)+salario)