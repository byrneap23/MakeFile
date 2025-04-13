a = 1
b = 2
c = 3


outFile = open("number1.txt","w")

outFile.write(str(a) + " + " + str(b) + " = " + str(a+b) + "\n")
outFile.write(str(c) + " + " + str(b) + " = " + str(c+b) + "\n")
outFile.write(str(b) + " - " + str(a) + " = " + str(b-a) + "\n")
outFile.write(str(c) + " - " + str(b) + " = " + str(c-b) + "\n")
outFile.write(str(c) + " - " + str(a) + " = " + str(c-a) + "\n")
