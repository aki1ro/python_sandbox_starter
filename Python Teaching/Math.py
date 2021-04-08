

def recure(x):
   if x <= 0:
      return 0
   else:
      print(x)
      x = recure(x - 15)

x = recure(int(input()))




