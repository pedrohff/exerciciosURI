def calc(raio):
    return (4/3) * 3.14159 * pow(float(raio), 3)

r = input()
print("VOLUME = %.3f" %calc(r))