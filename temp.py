print("Supported temperature formats: 36.6 C | 97.88 F | 309.75 K")

while True:
    FROM = input("Temperature: ").upper().split()
    print(FROM)
    if len(FROM) != 2:
        print("Unsupported conversion format")
        continue
    if FROM[0].replace('.', '', 1).replace('-', '', 1).isdecimal():
        if FROM[1] == "C" or FROM[1] == "F" or FROM[1] == "K":
            VALUE = float(FROM[0])
            if FROM[1] == "C":
                kelvin = VALUE + 273.15
            elif FROM[1] == "F":
                kelvin = ((5/9) * (VALUE - 32) + 273.15)
            elif FROM[1] == "K":
                if VALUE < 0:
                    continue
                else:
                    kelvin = VALUE
            break
        else:
            print("Unsupported conversion format")
while True:
    TO = input("Convert to (C(elsius) | K(elvin) | F(ahrenheit)): ").upper()
    if TO == "C" or TO == "F" or TO == "K":
        if TO == "C":
            END = (kelvin - 273.15)
        elif TO == "F":
            END = (1.8 * (kelvin - 273.15) + 32)
        elif TO == "K":
            END = kelvin
        break
    else:
        print ("Unsupported conversion format. Please use one of the followings: C(elsius) | K(elvin) | F(ahrenheit)")

print("Conversion result: ",VALUE, FROM[1], '=', END, TO)