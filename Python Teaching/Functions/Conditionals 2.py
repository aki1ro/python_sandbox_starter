# i = 1
# while i >= 0:
#    print(i)
#    if i == 32000:
#       print("You're at the mark", i)
#    i += 1



# x, y, z = input().split()
        

points = 100
i = 0
while i < 4:
   if input("Enter hit or miss:") == "hit":
      points += 10
   else:
      points -= 20
   i += 1

x = input()
y = input()
z = input()
v = input()


def hom(*args):
   points = 100
   for h in args:
      if h == "hit":
         points += 10
      else:
         points -= 20
   return points
      
hom(x,y,z,v)

   
print(points)

list = [x,y,z,v]

i = list

def hit_or_miss(i):
   points = 100
   for u in i:
      if u == "hit":
         points += 10
      elif u == "miss":
         points -= 20
   return points
       
print(hit_or_miss(i))

points = 100

x = input()
if x == "hit":
    points += 10
elif x == "miss":
        points -=20

x = input()
if x == "hit":
    points += 10
elif x == "miss":
        points -=20

x = input()
if x == "hit":
    points += 10
elif x == "miss":
        points -=20

x = input()
if x == "hit":
    points += 10
elif x == "miss":
        points -=20

print(points)


# sum = 0 
# while True:
#     x = input()
#     if x == "stop":
#         break
#     else:
#         x = int(x)
#     sum += x
# print(sum)

# i = 1
# while i >= 0:
#    print(i)
#    i += 1
#    if i == 32000:
#       print("You're at the mark", i)
#    elif i > 32000:
#        break

# for i in range(32001):
#    print(i)
#    if i == 32000:
#       print("You're at the mark", i)


# points = 100


# x = input()
# if x == "hit":
#     points += 10
# elif x == "miss":
#         points -=20

# x = input()
# if x == "hit":
#     points += 10
# elif x == "miss":
#         points -=20

# x = input()
# if x == "hit":
#     points += 10
# elif x == "miss":
#         points -=20

# x = input()
# if x == "hit":
#     points += 10
# elif x == "miss":
#         points -=20

# print(points)

# sum = 0 
# while True:
#     x = input()
#     if x == "stop":
#         break
#     else:
#         x = int(x)
#     sum += x
# print(sum)

