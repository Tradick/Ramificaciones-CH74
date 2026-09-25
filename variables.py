#Variable: espacio en memoria que se usa para almacenar cierto tipo de dato

#Tipos de variables

#Guardamos texto dentro de una variable llamada nombre
'''
nombre='Ricardo'
print(nombre)
print(type(nombre))

edad=25
city='México'
print(edad, city )
#print(type(edad, city)) thhis one didn't work bc type takes 1 or 3 arguments
'''
#enteros:  int
num1, num2= 5, 10
print(num1, num2)

#operadores
print('la suma es: ' + str(num2+num1))  #output: 15
print('la resta de 5-10 es:'+str(num1-num2))  #output: -15
print('la multiplicación es: ',num1*num2) #output: 50
print('La división es: ',num1/num2)  #output: 0.5
print('La divisón entera es: ',num1//num2) #DIVISIÓN ENTERA, quita los decimales

#flotantes (float) o (double), diferencia: espacio en memoria:
precio_1=99.99
calif=-5.0
print(precio_1+calif)
print('La clase de calif es: ',type(calif))

#Booleanos o bool (verdadero ó falso, 1 ó 0)
activo= True 
finalizado= False
cero=0 #la clase no da bool, da int
cero2='0' #la clase ahora es str
cero3=int('0') #la clase es int nuevamente
print(type(activo), type(finalizado), type(cero))