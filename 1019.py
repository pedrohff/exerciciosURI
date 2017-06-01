tempo = int(input())

hora = tempo // 3600
horamod = tempo % 3600

minutos = horamod // 60
minmod = horamod % 60

print("%d:%d:%d" %(hora,minutos,minmod))