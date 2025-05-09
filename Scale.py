weight = float(input("Weight: "))
unit = input("kg (K) or Lbs (L) : ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weigt in LBS: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))
