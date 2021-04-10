# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object


class Budget:
   subtotal = 0
   def __init__(self, total,category):
      print(f"Current Budget: {total}")
      self.funds = total
      self.category = category

   def withdraw(self, amount):
      self.funds += amount
      Budget.subtotal -= amount
      print(f"You've removed {amount} funds from {self.category}")
      return self.funds and print(f"Total remaining on Budget: {self.funds}")
      
   def deposit(self, amount):
      self.funds -= amount
      Budget.subtotal += amount
      print(f"You've Deposited {amount} funds into {self.category}")
      return self.funds and print(f"Total remaining on Budget: {self.funds}")
     
   

   def review(self):
      pass
   
   def total(self):
      pass
   
   # def transfer(self):

# class food(Budget):
#    def __init__(self):
#       self.subtotal = Budget.subtotal
#       super.__init__(self.total, self.subtotal, "Food")
#       return self.subtotal

# class clothing(Budget):
#    def __init__(self):
#       self.subtotal = Budget.subtotal
#       super.__init__(self.total, self.subtotal, "Clothing")
#       return self.subtotal

# class entertainment(Budget):
#    def __init__(self):
#       self.subtotal = Budget.subtotal
#       super.__init__(self.total, self.subtotal, "Entertainment")
#       return self.subtotal


def select(total = int(input("Enter Budget Amount: "))):
   while total > 0:
      t = total
      c = input("Select Category to allocate budget(food,clothing,entertainment):")
      o = input("Select Option(save,spend,review,end): ")
      if o == "save":
         a = int(input("Enter amount to save: "))
         b = Budget(t,c)
         b.withdraw(a)
      elif o == "spend":
         a = int(input("Enter amount to spend: "))
         b = Budget(t,c)
         total = b.deposit(a)
      elif o == "review":
         c.review()
      else:
            continue
   else:
      pass
      
      


select()









   

   




