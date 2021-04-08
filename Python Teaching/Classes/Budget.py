# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object


class Budget:
   def __init__(self, total, subtotal, category):
      print(f"Current Budget: {total}")
      self.funds = total
      self.subfunds = subtotal
      self.category = category

   def withdraw(self, amount):
      self.funds += amount
      self.subfunds -= amount
      print(f"You've removed {amount} funds from {self.category}")
      return self.funds and print(f"Total remaining on Budget: {self.funds}")

   def deposit(self, amount):
      self.funds -= amount
      self.subfunds += amount
      print(f"You've Deposited {amount} funds from {self.catagory}")
   
   def review(self):
      print()
   
   def total(self):
      print()

   
   # def transfer(self):

class food(Budget):
   def __init__(self):
      self.subtotal = subtotal
      super().__init__(self.subtotal, "Food")

class clothing(Budget):
   def __init__(self):
      self.subtotal = subtotal
      super().__init__(self.subtotal, "Clothing")

class entertainment(Budget):
   def __init__(self):
      self.category = category
      self.subtotal = subtotal
      super().__init__(self.total, self.subtotal, "Entertainment")


def select(total = int(input("Enter Budget Amount: ")),subtotal = 0):
   while total > 0:
      t = total
      s = subtotal
      c = input("Select Category to allocate budget(food,clothing,entertainment):")
      o = input("Select Option(save,spend,review,end): ")
      if o == "save":
         a = int(input("Enter amount to save: "))
         b = Budget(t,s,c)
         b.withdraw(a)
      elif o == "spend":
         a = int(input("Enter amount to spend: "))
         b = Budget(t,s,c)
         b.withdraw(a)
      elif o == "review":
         c.review()
      else:
            continue
   else:
      Budget.total()
      



select()









   

   




