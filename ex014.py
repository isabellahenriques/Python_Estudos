#Escreva um program que converta uma temperatura digitada em graus celcius e converta para graus fahrenheit
celcius = float(input("Qual a temperatura em graus ºC: "))
fahrenheit = (1.8 * celcius + 32)
kelvin = (celcius + 273)
print("A temperatura de {} ºC equivale a {} ºF ou {} ºK.".format(celcius, fahrenheit, kelvin))

