def greet(lang): #def function(x)
    if lang =='es':
      return('Hola')
    elif lang == 'fr':
        return('Bounjour')
    else:
        return('Hello')



print(greet('en'), 'Glen')
print(greet('es'), 'Camila')
print(greet('fr'), 'Sally')

###############################

def suma(a,b):
    sumar =a+b
    return sumar

x= suma(3,5)
print(x)


