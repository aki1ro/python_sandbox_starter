#Class is a blueprint for creating instances, anything created from it is an instanced of that class

class Employee:
   
      def __init__(self, first, last, pay): # <--- constructor
         self.first = first # <---- Attribute assigned to class
         self.last = last
         self.email = (f"{first}.{last}@gmail.com")
         self.pay = pay
      
      def fullname(self):
         return (f'{self.first} {self.last}')

emp_1 = Employee('Nick',"Endrikat",100000) # <--- this is an instance of a class
emp_2 = Employee('Test', 'User', 213411)

print(emp_1)
print(emp_2)

#Rather than doing this, you can create a class for them
# emp_1.first = "Nick"
# emp_1.last = "Endrikat"
# emp_1.email = "nickendrikat@gmail.com"
# emp_1.pay = 100000

print(emp_1.pay)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

print(Employee.fullname(emp_1))
