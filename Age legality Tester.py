agecutoffsmoke = 18

agecutoffdrink = 21


age = int(input("Are you legal to Drink or Smoke? Enter Age: "))

if agecutoffsmoke <= age:
   age = age   
else:print("You are not legal to Smoke or Drink")
if agecutoffsmoke <= age:
      if agecutoffdrink > age:
         print("You are legal to Smoke, but not Drink")
      else:
         print("You are Legal to Drink and Smoke")
         # if agecutoffdrink <= age:
         #    print("You are legal to Drink and Smoke")

input("Press Enter to exit")


