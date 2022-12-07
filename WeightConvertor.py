#Converts weight from Kilos to lbs
w=int(input("Weight: "))
p=str(input("Convert into (L)for lbs or (K)for kilos: "))
if p.upper() =="L":
    converted = w*2.204
    print(f"You are {round(converted)} pounds")
elif p.upper() =="K":
    converted = w/2.204
    print(f"You are {round(converted)} kilos")
else:
    print(f"Wrong Input")


