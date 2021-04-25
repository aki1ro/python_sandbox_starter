a = '\n  ###\n  #\n  ###\n    #\n  ###'

b = '\n  ###\n  #\n  ###\n    #\n  ###'

# print(a + b)

# a = 'nick'

# b = 'endrikat'

# print(a + b)
def ledmaker(number):
  number = str(number)
  led = []
  for i in number:
    if i == "1":
      i = '''
  #
  #
  #
  #
  #'''
      led.append(i)
    elif i == "2":
      i = '''
  ###
    #
  ###
  #    
  ###'''
      led.append(i)
    elif i == "3":
      i = '''
  ###
    #
  ###
    #
  ###'''
      led.append(i)
    elif i == "4":
      i = '''
  # #
  # #
  ###
    #
    #'''
      led.append(i)
    elif i == "5":
      i = '''
  ###
  #
  ###
    #
  ###'''
      led.append(i)
    elif i == "6":
      i = '''
  ###
  #
  ###
  # #
  ###'''
      led.append(i)
    elif i == "7":
      i = '''
  ###
    #
    #
    #
    #'''
      led.append(i)
    elif i == "8":
      i = '''
  ###
  # #
  ###
  # #
  ###'''
      led.append(i)
    elif i == "9":
      i = '''
  ###
  # #
  ###
    #
  ###'''
      led.append(i)
    elif i == "0":
      i = '''
  ###
  # #
  # #
  # #
  ###'''
      led.append(i)
  print(led)
  final_led(led)


def final_led(*led):
  return led


print(ledmaker(1))

  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###

