# تو چقدر اضافه وزن داری؟

# https://quera.org/problemset/3404/

n = float(input())
m = float(input())
BMI = n/(m**2)

print("%.2f" % BMI)

if BMI < 18.50 :
    print("Underweight")
elif 18.50 <= BMI < 25 :
    print("Normal")
elif 25 <= BMI < 30 :
    print("Overweight")
else :
    print("Obese")