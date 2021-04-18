#My own split function.


def mysplit(strng):
   mysplit = []
   fnd = strng.find(' ')
   mysplit.append(strng[:strng.find(' ')])
   while fnd != -1:
      fnd1 = strng.find(' ', fnd + 1)
      if fnd1 == -1:
         mysplit.append(strng[fnd + 1::])
      else:
         mysplit.append(strng[fnd + 1:fnd1])
      # print(fnd)
      fnd = strng.find(' ', fnd + 1)
   for i in mysplit:
      if i == '' or i == ' ' or i == "":
         mysplit.remove(i)
   if '' in mysplit:
      return []

   return mysplit

     
      


  



print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

