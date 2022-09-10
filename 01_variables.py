#Variables
my_string_variable = "My String variable" 
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

#Variables en una sola linea
name, surname, alias, age = "Juan", "Larrota", "Yuuto", 26
print("mi nombres es:",name,surname,". Mi edad es: ",age,"y mi alias es:",alias)

#Cambiar el tipo de variable
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

#Concatenacion de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de: ",my_bool_variable)

#Algunas funciones del sistema
#len() cuenta la cantidad de caracteres 
print(len(my_string_variable)) #18 

#Ingreso por pantalla

'''
name = input("What is your name?")
age = input("How old are you?")
print(name)
print(age)
'''

#Cambiamos tipo de datos
name = 26
age = "juan"
print(name)
print(age)

#Forzamos el tipo?
adress : str = "Esta es mi direccion"
adress = 32
print(type(adress))

