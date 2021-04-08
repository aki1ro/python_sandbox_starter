x = 8

print(x != 4) #not equal to 
print(x == 8) #equal to
print(x >= 11) #greater than or equal to
print(x <= 210) #less than or equal to
print(x > 8) #greater than
print(x < 2) #less than


my_list = [1, 2, 3]

for v in range(len(my_list)):
   print(my_list[v])
   my_list.insert(1, my_list[v])
print(my_list)