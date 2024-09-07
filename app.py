nombre = input("Por favor, ingresa tu nombre: ") 
apellido = input("Por favor, ingresa tu apellido: ") 


print("¡Hola,", nombre, apellido + "!")


precio = 100 
descuento = 0.15 

precio_final = precio - (precio * descuento) 

print(precio_final) 


edad = int(input("Introduce tu edad: ")) 
if edad >= 18: 
  print("Eres mayor de edad.") 
else: 
  print("Eres menor de edad.") 
  
  
numero = int(input("Introduce un número: ")) 
if numero % 2 == 0: 
  print(numero, "es un número par.") 
else: 
  print(numero, "es un número impar.") 
  
  
num1 = float(input("Introduce el primer número: ")) 
num2 = float(input("Introduce el segundo número: ")) 

suma = num1 + num2 
resta = num1 - num2 

multiplicacion = num1 * num2 
if num2 != 0: 
  division = num1 / num2 
else: 
  division = "No se puede dividir entre cero" 
print("Suma:", suma) 
print("Resta:", resta) 
print("Multiplicación:", multiplicacion) 
print("División:", division)     


calificacion = int(input("Introduce tu calificación: ")) 
if calificacion >= 70: 
  print("Aprobado") 
else: 
  print("Reprobado") 
  

num1 = float(input("Introduce el primer número: ")) 
num2 = float(input("Introduce el segundo número: ")) 
if num1 > num2: 
  print(num1, "es mayor que", num2) 
elif num2 > num1: 
  print(num2, "es mayor que", num1) 
else: 
  print("Los números son iguales.")  
  

nombre = input("Por favor, ingresa tu nombre: ") 
print("¡Bienvenido/a, " + nombre + "!")  


numero = int(input("Introduce un número: ")) 
print("Tabla de multiplicar del", numero, ":") 
for i in range(1, 11): 
  resultado = numero * i 
  print(numero, "x", i, "=", resultado)
  
num1 = float(input("Introduce el primer número: ")) 
num2 = float(input("Introduce el segundo número: ")) 
promedio = (num1 + num2) / 2 
print("El promedio de los dos números es:", promedio)   