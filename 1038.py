itens = {
    1: 4.0,
    2: 4.5,
    3: 5.0,
    4: 2.0,
    5: 1.5
}

input = input()
valores = [int(x) for x in input.split(" ")]

total = itens[valores[0]] * valores[1]

print("Total: R$ %.2f" %total)
