print("TIENDA DON PEPE")

monto = float(input("ingrese el monto: "))
Dia = input("ingrese el dia: ")
descuento = monto * 0.15
if Dia == "martes" :
    preciofinal = monto - descuento
    print("el precio a pagar es:", preciofinal)
    print("el descuento es de:", descuento)
elif Dia == "jueves":
    preciofinal = monto - descuento
    print("el precio a pagar es:", preciofinal)
    print("el descuento es de:", descuento)
else:
    print("El total a pagar es:", monto)