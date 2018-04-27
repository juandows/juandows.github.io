# -*- coding: utf-8 -*-


# (%riesgo*capital)/(PC-PV) = nº acciones, ej.- (0.002*10000)/(10-9) = 200 acciones a 10 €, stop loss 9
# (%riesgo*capital)=  (PC-PV)*acciones
# (%riesgo*capital) + PV*acciones = PC*acciones
# PV = ( (PC*acciones) - (%riesgo*capital) )/acciones
PC = 8.20
acciones = 121
riesgo = 0.02
capital = 1000
PV = ( (PC*acciones) - (riesgo*capital) )/acciones
stoploss = PV-PC
precioactual = 8.40
print PV
print 1-PV/PC
print stoploss
print precioactual+stoploss
