# Codelab Variables Python
#   1.Crear un nuevo repositorio en tu Github para alamcenar este y sucesivos proyectos del curso
#   2.Crea un nuevo archivo .py
#   3.Define una variable de cada tipo de primitivo
# I. Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable
#       Enteros
n1 = "8"
n2 = "6"
print (int(n1) + int(n2))
#       Flotantes 
n1 = "8.5"
n2 = "6.3"
print (float(n1) + float(n2))
#       Booleanos
booleano = 32 > 42
print(booleano)
#       String 
str("Hola mundo")
print("Hola mundo")

# II. Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo

# Números enteros – int

#Los números enteros representan a los números naturales más el 0 pudiendo ser positivos o negativos y tienen las siguientes características:

#Están en una base concreta (por defecto base 10).
#Pueden ser negativos o positivos o cero (0).
#Pueden realizarse operaciones entre ellos.
#Son el tipo base, por lo que se pueden realizar operaciones con otros tipos fácilmente.
#En Python 3 no hay límite de tamaño de estos números.

# Números flotantes 

#Los float a diferencia de los int tienen unos valores mínimo y máximos que pueden representar. La mínima precisión es 2.2250738585072014e-308 y la máxima 1.7976931348623157e+308, pero si no nos crees, lo puedes verificar tu mismo.

# III. Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable

# La fórmula para calcular la suma de los primeros n números pares es:
#Suma = n * (n + 1)
#Donde "n" es la cantidad de números pares que deseas sumar.

n = int(input("Ingresa el número entero positivo "))
suma = n * (n + 1)
print(f"La suma de los primeros {n} números pares es: {suma}")
