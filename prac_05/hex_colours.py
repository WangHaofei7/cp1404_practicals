NAME_TO_CODE = {
"Aqua": "#00ffff", "Ash Grey": "#b2beb5", "Baker-Miller Pink": "#ff91af",
"Bitter Lemon": "# cae00d", "Bole": " # 79443b", "Brilliant Rose": "#ff55a3",
"Brown": "#a52a2a", "Buff": "#f0dc82", "Cameo Pink": "#efbbcc",
"Dark Pastel Green": "#03c03c"
}

colour_name = input("Enter a colour name: ").title()
while colour_name != "":
    try:
        print(f"{colour_name}'s code is : {NAME_TO_CODE[colour_name]}")
    except KeyError:
        print("Unable to find corresponding name")
    colour_name = input("Enter a colour name: ").title()