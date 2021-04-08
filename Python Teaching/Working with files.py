myfile = open("classes.py")

myfile = open("Class Methods.py", "w")

myfile = open("Data Hiding.py", "r")

myfile = open("Exceptions.py", "a")

myfile = open("Math.py", "wb") #can also add rb, ab, etc. 

myfile.close() #function to close

myfile = open("text.txt")
print(myfile.read())
myfile.close()

myfile = open("text.txt")
print(myfile.read(3))
print(myfile.read(4))
print(myfile.read())
myfile.close()

myfile1 = open("text.txt")

# for line in myfile.readlines():
#    print(line)

line = myfile1.readlines()

print(line[3])



myfile = open("newtext.txt", "w")

myfile.write(f"This is a new file I wrote in using write function {line}")

myfile.close
myfile = open("newtext.txt", "a")

x = myfile.write(input()) # also returns the number of bytes written as seen with print(x)
print(f"Number of Bytes Written: {x}") 

myfile.close

n = int(input())

file = open("numbers.txt", "w+")

for i in range(1, n+1):
    file.write(f"{i}\n")

file.close

file = open("numbers.txt", "r")
print(file.read())

file.close

with open("numbers.txt", "a") as f:
   f.write(input())

with open("numbers.txt") as f:
   print(f.read())

with open("books.txt") as f:
    l = f.readlines()
    n = 1
    for i in l:
       w = 0
       w = i.count(" ") + 1
       if w != 1:
          print(f"Line {n}: {w} words")
       else:
          print(f"Line {n}: {w} word")
       n += 1

file = open("books.txt", "r")
r = file.readlines()
for i in r:
    ev = i.split()
    end = ""
    for en in ev:
       env = en[0]
       end = end + env
    else:
       print(end)



file.close()









