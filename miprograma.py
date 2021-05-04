nombre = input('Por favor, escriba su nombre: ')
apellido = input ('Por favor, escriba su apellido: ')
edad = input ('ingrese su edad: ')
edad = int(edad)
if edad <18:
    condicion='Menor'
elif edad >= 18 and edad < 65:
    condicion='Mayor'
elif edad >= 65 and edad <= 130:
    condicion='Jubilado'
else:
    condicion='Cadaver'
print('Su nombre es: '+nombre+ ' y su apellido es: ' + apellido + ' y por su edad usted es un: ' + condicion)
