dias = int(input())

anos = dias // 365
meses = (dias%365) // 30
dias = (dias%365) % 30

print("%d ano(s)" %anos)
print("%d mes(es)" %meses)
print("%d dia(s)" %dias)