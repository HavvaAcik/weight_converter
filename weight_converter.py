# phyton weight converter 

weight = float(input("Kilonuzu yazınız: "))
unit =input("Kg mı Pound mu? (K/P)")

if unit == "K" :
    weight = weight * 2.205
    unit = "lbs"
    print(f"kilonuz: {round(weight)} {unit}")
elif unit == "P" :
    weight = weight / 2.205
    unit = "kg"
    print(f"kilonuz: {round(weight)} {unit}")
else :
    print("Geçerli bir değer giriniz.")

    
