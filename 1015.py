from math import sqrt
inputA = input()
inputB = input()

x1 = float(inputA.split(" ")[0])
y1 = float(inputA.split(" ")[1])
x2 = float(inputB.split(" ")[0])
y2 = float(inputB.split(" ")[1])

resultado = sqrt(pow((x2-x1),2) + pow((y2-y1),2))

print("%.4f"%resultado)