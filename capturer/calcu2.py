# -*- coding: utf-8 -*-


valores = ["TEL","SAN","REE","CAT","IBE","IND","GAS","IDR","ACS","DIA"]
#valores = ["TEL","SAN","REE","CAT","IBE","ACS"]
valoracion2015 = [11.36,5.79,18.25,24.87,5.59,23.79,19.45,7.76,29.22,5.30]
valoracion2016 = [09.68,3.95,18.70,23.40,6.30,27.11,15.27,8.81,22.35,4.86]
valoracion2017 = [09.09,5.05,17.20,31.21,6.01,31.93,17.88,10.63,30.42,4.73]
valoracion2018 = [08.37,6.06,17.61,36.70,6.74,29.60,20.37,11.68,33.66,4.54]

aportaciones = [1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0]
acciones = [0,0,0,0,0,0,0,0,0,0]
valor2015 = [0,0,0,0,0,0,0,0,0,0]
valor2016 = [0,0,0,0,0,0,0,0,0,0]
valor2017 = [0,0,0,0,0,0,0,0,0,0]
valor2018 = [0,0,0,0,0,0,0,0,0,0]
for x in range(10):
    acciones[x] = round(aportaciones[x]/valoracion2015[x], 2)
    valor2015[x]= round(acciones[x]*valoracion2015[x], 2)
    valor2016[x]= round(acciones[x]*valoracion2016[x], 2)
    valor2017[x]= round(acciones[x]*valoracion2017[x], 2)
    valor2018[x]= round(acciones[x]*valoracion2018[x], 2)

print valores
print valor2015
print valor2016
print valor2017
print valor2018
print sum(valor2018)
