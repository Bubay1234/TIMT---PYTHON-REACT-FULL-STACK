temp = float(input("Enter temperature: "))

if temp >= 40:
    print("Very Hot - Stay indoors")
elif temp >= 30:
    print("Hot - Stay hydrated")
elif temp >= 20:
    print("Normal Weather")
elif temp >= 10:
    print("Cool Weather")
else:
    print("Very Cold - Wear warm clothes")