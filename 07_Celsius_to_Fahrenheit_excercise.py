C = -20
for C in range(-20,41,5):
    print("%+5.0f °C" % C, end="")
    F = (212-32)*(C/100)+32
    print("%+5.0f °F" % F)

