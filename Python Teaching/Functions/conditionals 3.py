# points = 100
# inputs = 0
# while inputs != 4:
#     inputs += 1
#     x = input()
#     if x == "hit":
#        points += 10
#     elif x == "miss":
#        points -= 20

# print(points)

# print(total_price)
# passenger = 0
# total_price = 0
# while passenger != 5:
#     passenger += 1
#     x = int(input())
#     if x >= 3:
#         total_price += 100
#     else:
#         continue

# w = int(input())
# h = float(input())

# Weight is in kg, height is in meters

# BMI = w/h**2

# if BMI < 18.5:
#     print("Underweight")
# elif BMI >= 18.5 and  BMI < 25:
#     print("Normal")
# elif BMI >= 25 and BMI < 30:
#     print("Overweight")
# elif BMI >= 30:
#     print("Obesity")
'''
You’re making a gold purity checker, that should accept only 22K or 24K gold. Only the good stuff!

22K gold has 91.7% or more gold in it, while 24K corresponds to 99.9% and above purity.

Given the % of gold purity as input, you should output "Accepted" only if it corresponds to 22 or 24K.
'''
purity = float(input())

if purity >= 99.9:
    print("Accepted")
elif purity < 99.9 and purity >= 91.7:
    print("Accepted")
