# -*- coding: utf-8 -*-

def ingresos( cantidad, rentabilidad ):
   "This prints a passed string into this function"
   result = cantidad*rentabilidad
   print "Generados "+str(result)+"€"
   return result

#ingreso de 1000 anuales
rentabilidad = 0.04
anios = 20
saldoIni = 0
saldo=saldoIni
print "Saldo inicial "+str(saldo)+"€"
saldo += ingresos(saldo, rentabilidad)
print "Saldo final "+str(saldo)+"€"
for i in range(0, anios-1):
    saldo += 1000
    print "Saldo año "+str(i+1)+" "+str(saldo)+"€"
    saldo += ingresos(saldo, rentabilidad)
    print "Saldo con ingresos año "+str(i+2)+" "+str(saldo)+"€"
print "Resultado "+str(anios)+" años: ingresado("+str(saldoIni+1000*anios)+") ingresos("+str(saldo-(saldoIni+1000*anios))+")"

#ingreso 1000 y otros 1000 a medio año
saldo=saldoIni
print "Saldo inicial "+str(saldo)+"€"
saldo += ingresos(saldo, rentabilidad)
saldo += 1000 + ingresos(1000, rentabilidad/2)
print "Saldo final "+str(saldo)+"€"
for i in range(0, anios-1):
    saldo += 1000
    print "Saldo año "+str(i+2)+" "+str(saldo)+"€"
    saldo += ingresos(saldo, rentabilidad)
    saldo += 1000 + ingresos(1000, rentabilidad/2)
    print "Saldo con ingresos año "+str(i+1)+" "+str(saldo)+"€"

saldo += ingresos(saldo, rentabilidad)
print "Resultado "+str(anios)+" años: ingresado("+str(saldoIni+1000*anios*2)+") ingresos("+str(saldo-(saldoIni+2000*anios))+")"

#ingreso 1000 y otros 1000 a medio año gastando ingresos
saldo=saldoIni
ingresosTotal = 0
print "Saldo inicial "+str(saldo)+"€"
ingresosTotal += ingresos(saldo, rentabilidad)
saldo += 1000
ingresosTotal += ingresos(1000, rentabilidad/2)
print "Saldo final "+str(saldo)+"€"
for i in range(0, anios-1):
    saldo += 1000
    print "Saldo año "+str(i+1)+" "+str(saldo)+"€"
    ingresosTotal += ingresos(saldo, rentabilidad)
    saldo += 1000
    ingresosTotal += ingresos(1000, rentabilidad/2)
    print "Saldo con ingresos año "+str(i+2)+" "+str(saldo)+"€"

ingresosTotal += ingresos(saldo, rentabilidad)
print "Resultado "+str(anios)+" años: ingresado("+str(saldoIni+1000*anios*2)+") ingresos("+str(saldo-(saldoIni+2000*anios)+ingresosTotal)+")"
