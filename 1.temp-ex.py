temp = float(input("Enter the temperature in °C: "))

if temp < 0:
    print("Cold")
elif temp < 10:
    print("chill")
elif temp < 25:
    print("Mild")
elif temp < 50:
    print("warm")
else:
    print("hot")