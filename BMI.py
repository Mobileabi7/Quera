n = float(input())
m = float(input())
BMI = n/(m**2)
if BMI < 18.50 :
    print(round(BMI,2))
    print("Underweight")
elif 18.50 <= BMI < 25 :
    print(round(BMI,2))
    print("Normal")
elif 25 <= BMI < 30 :
    print(round(BMI,2))
    print("Overweight")
else :
    print(round(BMI,2))
    print("Obese")