weight = input("What do you want to convert?: ")
measure, units = weight.split(" ")
measure = int(measure)
def conversion(measure, units):
    pound = ["pound", "pounds" ,"lbs"]
    ounce = ["ounce", "ounces", "oz"]
    gram = ["gram", "grams", "g"]
    kilogram = ["kilogram", "kilograms", "kg"]

    kg = 0
    lb = 2.205
    oz = 35.274
    g = 1000

    if(units in pound):
        kg = measure / lb
    elif(units in ounce):
        oz = measure / oz
    elif(units in gram):
        g =units / g
    elif(units in kilogram):
        kg = measure
    print(f"{measure} {units} = {round(kg, 3)} kg")
    print(f"{measure} {units} = {round(kg * lb, 3)} lb")
    print(f"{measure} {units} = {round(kg * oz, 3)} oz")
    print(f"{measure} {units} = {round(kg * g, 3)} g")
    return

conversion(measure, units)