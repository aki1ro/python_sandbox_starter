def led_maker():
    number = 6
    digits = {'1': "  #\n  #\n  #\n  #\n  #", '2': "  ###\n    #\n  ###\n  #    \n  ###", '3': "  ###\n    #\n  ###\n  #\n  ###", '4': "  # #\n  # #\n  ###\n    #\n    #", '5': "  ###\n  #\n  ###\n    #\n  ###", '6': "  ###\n   #\n  ###\n  # #\n  ###", '7': "  ###\n      #\n    #\n    #\n    #", '8': "  ###\n  # #\n  ###\n  # #\n  ###", '9': "  ###\n  # #\n  ###\n    #\n  ###", '0': "  ###\n  # #\n  # #\n  # #\n  ###"}
    to_print = [digits[i].split('\n') for i in list(str(number))]
    for t in zip(*to_print):
        print(*t) # <----  * in this case is used to extract the tuple and print it
    


led_maker()



